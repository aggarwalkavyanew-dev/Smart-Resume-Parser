# Smart Resume Parser

## Project Overview
The **Smart Resume Parser** is a Python-based application that extracts structured information from resumes (PDF and DOCX). It automatically identifies key sections such as **skills**, **education**, and **experience**, and outputs the results in **JSON** or **CSV** formats. The project also includes a **Streamlit web interface** for easy resume uploads and results visualization.

---

## Features
- Extract **skills**, **education**, and **experience** from resumes.
- Supports both **PDF** and **DOCX** formats.
- Outputs structured data in **JSON** or **CSV**.
- Web UI for uploading and previewing resumes.
- Easy to extend with custom skills lists and patterns.

---

## Tech Stack
- **Python 3.10+**  
- **PyMuPDF (fitz)** → PDF text extraction  
- **python-docx** → DOCX text extraction  
- **spaCy** → Natural Language Processing  
- **Regex** → Pattern matching for skills, degrees, and experience  
- **Streamlit** → Web UI  

---

## Installation

1. Clone the repository:  
```bash
git clone https://github.com/yourusername/smart-resume-parser.git
cd smart-resume-parser
```
2. Create a virtual environment:
   
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3.Install dependencies:
```
pip install -r requirements.txt
```

4.Download the spaCy English model:
```
python -m spacy download en_core_web_sm

```
