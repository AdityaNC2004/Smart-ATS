# Smart ATS

Smart ATS is an advanced AI-powered Resume Evaluation System designed to help candidates optimize their resumes for Applicant Tracking Systems (ATS). This application leverages Google's Generative AI to evaluate resumes against specific job descriptions, providing actionable insights to enhance resume alignment with job requirements. 

## Features

- Evaluate resumes against job descriptions with a percentage match.
- Identify missing keywords in the resume.
- Provide actionable feedback and recommendations to improve the resume.
- Supports PDF resume uploads.
- SmartATS : https://smartats03.streamlit.app

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AdityaNC2004/Smart-ATS.git
    cd smart-ats
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    Create a `.env` file in the root directory of your project and add your Google API key:

    ```plaintext
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload your resume (PDF format) and paste the job description.

4. Click "Submit" to get a detailed evaluation of your resume.

## Code Overview

### `app.py`

This is the main file of the Streamlit application. It contains the following key functions:

- `get_gemini_response(input)`: Sends a request to Google's Generative AI to get the response based on the input prompt.
- `input_pdf_text(uploaded_file)`: Extracts text from the uploaded PDF resume.
- Streamlit UI elements to upload the resume, input the job description, and display the results.

### Prompts

Two prompts (`input_prompt1` and `input_prompt2`) are used to interact with the Generative AI for detailed resume evaluation against job descriptions.

## Contributing

Contributions are welcome! Please create a pull request with a detailed description of your changes.


