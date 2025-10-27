Smart Resume Parser
Project Overview

The Smart Resume Parser is a Python-based application that extracts structured information from resumes (PDF and DOCX). It automatically identifies key sections such as skills, education, and experience, and outputs the results in JSON or CSV formats. The project also includes a Streamlit web interface for easy resume uploads and results visualization.

Features

Extract skills, education, and experience from resumes.

Supports both PDF and DOCX formats.

Outputs structured data in JSON or CSV.

Web UI for uploading and previewing resumes.

Easy to extend with custom skills lists and patterns.

Tech Stack

Python 3.10+

PyMuPDF (fitz) → PDF text extraction

python-docx → DOCX text extraction

spaCy → Natural Language Processing

Regex → Pattern matching for skills, degrees, and experience

Streamlit → Web UI

Installation

Clone the repository:

git clone https://github.com/yourusername/smart-resume-parser.git
cd smart-resume-parser


Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt


Download the spaCy English model:

python -m spacy download en_core_web_sm

Usage
Run Streamlit App
streamlit run app.py


Open the provided URL in your browser (usually http://localhost:8501).

Upload a PDF or DOCX resume.

View extracted skills, education, and experience.

Export the data to CSV if needed.

Example JSON Output
{
  "skills": ["Python", "Machine Learning", "SQL"],
  "education": ["Bachelor of Science in Computer Science, XYZ University"],
  "experience": ["Software Engineer at ABC Corp, 3 years"]
}

Project Structure
smart-resume-parser/
│
├─ app.py              # Streamlit application
├─ parser.py           # Resume parsing logic (text extraction + NLP)
├─ requirements.txt    # Python dependencies
├─ test_resumes/       # Sample resumes for testing
├─ outputs/            # JSON/CSV output files
└─ README.md

How It Works

Text Extraction: Uses PyMuPDF for PDFs and python-docx for DOCX files.

Preprocessing: Cleans text, removes extra spaces, and normalizes line breaks.

Information Extraction:

Skills: Matches against a predefined skills list.

Education: Detects degrees and universities using keywords.

Experience: Identifies job roles, companies, and duration using regex and NLP.

Output: Saves structured data in JSON or CSV format.

UI: Streamlit interface allows easy file upload, preview, and export.

Future Improvements

Add custom NER models for better job title and company detection.

Include contact info extraction (email, phone).

Support bulk resume uploads.

Integrate machine learning to categorize skills automatically.