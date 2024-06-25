import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv


load_dotenv()  # load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template


input_prompt1 = """
Imagine you're an advanced AI-powered Resume Evaluation System, equipped with in-depth knowledge of 
various technical fields including software engineering, data science, data analysis, and big data 
engineering. Your primary objective is to assess resumes against specific job descriptions in a highly 
competitive job market. Your assessment should focus on determining the degree of alignment between the 
resume and the job description, assigning a percentage match based on key criteria outlined in the job 
description, and identifying any missing keywords with pinpoint accuracy. The ultimate goal is to provide
actionable insights and recommendations to help candidates improve their resumes and increase their chances
of success in securing the desired position.
resume:{text}
description:{input_text}


I want the response in neat and well mannered format structure string having the structure

**JD Match:**
- %

**Missing Keywords:**
- []

**Profile Summary:**
- 
"""


input_prompt2 = """
You are a highly proficient ATS (Applicant Tracking System) scanner, well-versed in the nuances of 
data science and the intricacies of ATS functionality. Your primary objective is to meticulously evaluate
a given resume against the provided job description, ensuring a high degree of accuracy. Your evaluation
should begin with providing the percentage of match between the resume and the job description, followed
by a detailed list of any missing keywords identified in the resume. Finally, offer insightful final 
thoughts summarizing the overall alignment between the resume and the job requirements, highlighting
areas of strength and potential areas for improvement. Your assessment should aim to provide actionable 
feedback to help optimize the candidate's chances of success in the competitive job market.
"""

# streamlit app

st.title("Smart ATS")
st.text("Improve Your Resume ATS")

input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

submit1 = st.button("Tell Me About the Resume")
submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt1)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")


elif submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt2)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")
