
# 📚 Fetch Research Papers  

This project fetches research papers from **PubMed** using the **NCBI Entrez API** and extracts relevant details such as **author information** and **company affiliations**.  

---

## 📁 Project Structure  

```
Fetch_Research_Papers/
│── .venv/                  # Virtual environment (optional)
│── __pycache__/            # Compiled Python files (auto-generated)
│── results.csv             # Output file containing fetched data
│── pubmed_fetcher.py       # Main script to fetch and parse research papers
│── pubmed_cli.py           # CLI tool for running the fetcher with parameters
│── pyproject.toml          # Dependency management file (Poetry)
│── Readme.md               # Project documentation (this file)
```

---

## 🔧 Installation & Setup  

### 1️⃣ Clone the repository  
```sh
git clone <repository-url>
cd Fetch_Research_Papers
```

### 2️⃣ Set up a virtual environment (optional but recommended)  
```sh
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 3️⃣ Install dependencies  
Using **Poetry**:  
```sh
poetry install
```
Alternatively, using **pip**:  
```sh
pip install -r requirements.txt
```

---

## 🚀 Running the Program  

### 📜 Fetch research papers from PubMed  
```sh
python pubmed_fetcher.py
```

### 🔍 Use the CLI tool for custom queries  
```sh
python pubmed_cli.py --query "cancer research"

or

poetry run get-papers-list "cancer research" -f results.csv
```

---

## 🛠 Tools & Libraries Used  

| Tool / Library       | Purpose |
|----------------------|---------|
| 🔹 **Requests**      | For making HTTP requests ([Docs](https://docs.python-requests.org/en/latest/)) |
| 🔹 **XML ElementTree** | For parsing XML responses ([Docs](https://docs.python.org/3/library/xml.etree.elementtree.html)) |
| 🔹 **Poetry**        | Dependency management ([Docs](https://python-poetry.org/)) |
| 🔹 **NCBI Entrez API** | Fetches PubMed data ([Docs](https://www.ncbi.nlm.nih.gov/books/NBK25497/)) |

---

