from PyPDF2 import PdfReader as pdf

def readFile(file):
    reader = pdf(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        
    return text