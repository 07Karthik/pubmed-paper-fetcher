
# 📚 Fetch Research Papers

This project fetches research papers from PubMed using the **NCBI Entrez API** and extracts relevant details such as author information and company affiliations.

## 📁 Project Structure

```
Fetch_Research_Papers/
│── results.csv             # Output file containing fetched data
│── pubmed_fetcher.py       # Main script to fetch and parse research papers
│── pubmed_cli.py           # CLI tool for running the fetcher with parameters
│── pyproject.toml          # Dependency management file (Poetry)
│── poetry.lock             # Dependency lock file
│── Readme.md               # Project documentation (this file)
│── .gitignore              # Git ignore file
```

## 🔧 Installation & Setup

### 1️⃣ Clone the repository

```sh
git clone https://github.com/07Karthik/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
```

### 2️⃣ Install dependencies

#### Using Poetry:

```sh
poetry install
```


## 🚀 Running the Program

### 🔍 Use the CLI tool for custom queries

```sh
python pubmed_cli.py --query "cancer research"
```

or using Poetry:

```sh
poetry run get-papers-list "cancer research" -f results.csv
```

## 🛠 Tools & Libraries Used

| Tool / Library      | Purpose                                         |
|---------------------|-------------------------------------------------|
| 🔹 Requests        | For making HTTP requests ([Docs](https://docs.python-requests.org/)) |
| 🔹 XML ElementTree | For parsing XML responses ([Docs](https://docs.python.org/3/library/xml.etree.elementtree.html)) |
| 🔹 Poetry          | Dependency management ([Docs](https://python-poetry.org/docs/)) |
| 🔹 NCBI Entrez API | Fetches PubMed data ([Docs](https://www.ncbi.nlm.nih.gov/books/NBK25500/)) |

---
