import streamlit as st
import os
from groq import Groq
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
import base64

GROQ_API_KEY = os.getenv("GROQ_API_KEY")



def generate_mcqs(syllabus):
    client = Groq(api_key=GROQ_API_KEY)

    prompt = f"""
    Based on the following syllabus, generate EXACTLY 25 unique multiple-choice questions (MCQs) along with their respective correct answers. Format each question as follows:

    Q1. [Question text]
    A. [Option A]
    B. [Option B]
    C. [Option C]
    D. [Option D]
    Correct Answer: [Letter of correct option]


    Syllabus:
    {syllabus}
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content

def create_pdf(mcqs, user_name, output_filename="mcqs.pdf"):
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    
    header_style = ParagraphStyle(
        'Header',
        parent=styles['Heading1'],
        alignment=TA_CENTER,
        spaceAfter=12
    )

    question_style = ParagraphStyle(
        'Question',
        parent=styles['BodyText'],
        spaceBefore=6,
        spaceAfter=6
    )

    content = []
    
    content.append(Paragraph(f"Multiple Choice Questions - {user_name}", header_style))
    content.append(Spacer(1, 12))

    questions = mcqs.split('\n\n')

    for question in questions:
        content.append(Paragraph(question.replace('\n', '<br/>'), question_style))
        content.append(Spacer(1, 6))

    doc.build(content)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

def main():
    st.title("MCQ Generator")

    user_name = st.text_input("Enter your name for the PDF header:")
    syllabus = st.text_area("Enter the syllabus content:")

    if st.button("Generate MCQs"):
        if syllabus and user_name:
            with st.spinner("Generating MCQs..."):
                mcqs = generate_mcqs(syllabus)
            
            st.success("MCQs generated successfully!")
            st.text_area("Generated MCQs:", value=mcqs, height=300)

            pdf_filename = "mcqs.pdf"
            create_pdf(mcqs, user_name, pdf_filename)

            st.markdown(get_binary_file_downloader_html(pdf_filename, 'PDF'), unsafe_allow_html=True)
        else:
            st.error("Please enter both your name and the syllabus content.")

if __name__ == "__main__":
    main()