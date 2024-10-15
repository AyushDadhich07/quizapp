import PyPDF2
import io

def extract_pdf_text(pdf_file):
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_file.read()))
    text_content = ""
    
    for page in pdf_reader.pages:
        text_content += page.extract_text()
    
    return text_content
