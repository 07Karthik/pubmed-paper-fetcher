import requests
import csv
import xml.etree.ElementTree as ET
import re
from typing import List, Dict, Optional

# Define constants
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
COMPANY_KEYWORDS = {"pharma", "biotech", "therapeutics", "biosciences", "laboratories", "inc.", "ltd.", "gmbh"}
EMAIL_REGEX = r'[\w\.-]+@[\w\.-]+\.\w+'

def fetch_pubmed_papers(query: str, max_results: int = 20) -> List[Dict[str, str]]:
    """
    Fetch research papers from PubMed API based on a given query.
    """
    try:
        search_url = f"{BASE_URL}esearch.fcgi?db=pubmed&term={query}&retmax={max_results}&retmode=json"
        response = requests.get(search_url, timeout=10)
        response.raise_for_status()

        search_results = response.json()
        pubmed_ids = search_results.get("esearchresult", {}).get("idlist", [])

        if not pubmed_ids:
            print("No results found.")
            return []

        details_url = f"{BASE_URL}efetch.fcgi?db=pubmed&id={','.join(pubmed_ids)}&retmode=xml"
        details_response = requests.get(details_url, timeout=10)
        details_response.raise_for_status()

        return parse_pubmed_xml(details_response.text)

    except requests.RequestException as e:
        print(f"Error fetching data from PubMed API: {e}")
        return []

def parse_pubmed_xml(xml_data: str) -> List[Dict[str, str]]:
    """Parses XML data from PubMed to extract paper details."""
    root = ET.fromstring(xml_data)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        pubmed_id = get_element_text(article, ".//PMID", "Unknown")
        title = get_element_text(article, ".//ArticleTitle", "No Title")
        pub_date = get_element_text(article, ".//PubDate/Year") or get_element_text(article, ".//ArticleDate/Year", "Unknown")

        non_academic_authors = []
        company_affiliations = set()
        corresponding_email: Optional[str] = None

        for author in article.findall(".//Author"):
            name = get_author_name(author)
            affiliations = [aff.text for aff in author.findall("AffiliationInfo/Affiliation") if aff.text]

            for affiliation in affiliations:
                aff_lower = affiliation.lower()
                if any(keyword in aff_lower for keyword in COMPANY_KEYWORDS):
                    non_academic_authors.append(name)
                    company_affiliations.add(affiliation)
                    if corresponding_email is None:
                        email_match = re.search(EMAIL_REGEX, affiliation)
                        if email_match:
                            corresponding_email = email_match.group(0)

        if company_affiliations:
            papers.append({
                "PubmedID": pubmed_id,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academic Author(s)": "; ".join(non_academic_authors),
                "Company Affiliation(s)": "; ".join(company_affiliations),
                "Corresponding Author Email": corresponding_email or "Not Available"
            })
    
    return papers

def get_element_text(element: ET.Element, path: str, default: str = "") -> str:
    """Retrieves text content from an XML element safely."""
    found = element.find(path)
    return found.text.strip() if found is not None and found.text else default

def get_author_name(author: ET.Element) -> str:
    """Extracts an author's full name from an XML element."""
    first_name = get_element_text(author, "ForeName", "")
    last_name = get_element_text(author, "LastName", "")
    return f"{first_name} {last_name}".strip() if first_name or last_name else "Unknown"

def save_to_csv(papers: List[Dict[str, str]], filename: str) -> None:
    """Saves the extracted paper details into a CSV file."""
    headers = ["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"]
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(papers)
        print(f"Results saved to {filename}")
    except IOError as e:
        print(f"Error saving CSV file: {e}")