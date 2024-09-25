# MCQ-Generator App

This repository contains a Python application that generates Multiple Choice Questions (MCQs) based on a given syllabus using the Groq API and Streamlit for the user interface. The app also creates a downloadable PDF of the generated MCQs.

## Features

- Generate 25 unique MCQs based on user-provided syllabus
- Create a downloadable PDF of the generated MCQs
- User-friendly web interface using Streamlit

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- A Groq API key (Sign up at [https://console.groq.com](https://console.groq.com) to obtain your API key)

## Installation

Follow these steps to set up the MCQ-Generator app on your local machine:

### Windows

1. Clone the repository:
   ```
   git clone https://github.com/mddanish004/MCQ-Generator.git
   cd MCQ-Generator
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### macOS/Linux

1. Clone the repository:
   ```
   git clone https://github.com/your-username/MCQ-Generator.git
   cd MCQ-Generator
   ```

2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root directory:
   ```
   touch .env
   ```

2. Open the `.env` file and add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

To run the MCQ-Generator app:

1. Ensure you're in the project directory and your virtual environment is activated.

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Open your web browser and go to `http://localhost:8501` (or the address provided in the terminal).

4. Enter your name and the syllabus content in the provided fields.

5. Click the "Generate MCQs" button to create the questions.

6. Once generated, you can view the MCQs in the app and download them as a PDF.

## Contributing

Contributions to the MCQ-Generator app are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Groq](https://www.groq.com/) for providing the API used in generating MCQs.
- [Streamlit](https://streamlit.io/) for the web app framework.
- [ReportLab](https://www.reportlab.com/) for PDF generation.
