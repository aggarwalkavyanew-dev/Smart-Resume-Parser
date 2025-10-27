# PDF extraction
import fitz  # PyMuPDF
import re

def extract_pdf_text(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# DOCX extraction
from docx import Document

def extract_docx_text(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text
def clean_text(text):
    text = text.replace('\n', ' ').replace('\r', ' ')
    text = ' '.join(text.split())
    return text


skills_list = ['Python', 'Java', 'SQL', 'Machine Learning', 'Excel']

def extract_skills(text):
    skills_found = [skill for skill in skills_list if skill.lower() in text.lower()]
    return skills_found

import spacy
nlp = spacy.load('en_core_web_sm')

def extract_education(text):
    education_keywords = ['Bachelor', 'Master', 'B.Sc', 'M.Sc', 'PhD']
    education = [line for line in text.split('.') if any(word in line for word in education_keywords)]
    return education

def extract_experience(text):
    doc = nlp(text)
    experience = []
    for sent in doc.sents:
        if re.search(r'\d+\s+years', sent.text):
            experience.append(sent.text)
    return experience


import json


def parse_resume(file_path, file_type='pdf'):
    if file_type == 'pdf':
        text = extract_pdf_text(file_path)
    else:
        text = extract_docx_text(file_path)

    text = clean_text(text)

    data = {
        'skills': extract_skills(text),
        'education': extract_education(text),
        'experience': extract_experience(text)
    }
    return data


# Example JSON output
output = parse_resume('sample_resume.pdf')
print(json.dumps(output, indent=2))

import streamlit as st
import pandas as pd

st.title("Smart Resume Parser")

uploaded_file = st.file_uploader("Upload a resume", type=['pdf', 'docx'])
if uploaded_file:
    file_type = uploaded_file.name.split('.')[-1]
    with open(f"temp.{file_type}", "wb") as f:
        f.write(uploaded_file.getbuffer())

    result = parse_resume(f"temp.{file_type}", file_type)

    st.subheader("Extracted Information")
    st.json(result)

    # Export CSV
    if st.button("Export to CSV"):
        df = pd.DataFrame([result])
        df.to_csv("output.csv", index=False)
        st.success("CSV saved!")

