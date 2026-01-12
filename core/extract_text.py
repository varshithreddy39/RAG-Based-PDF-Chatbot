from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    all_text = []

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            all_text.append(text)

    return " ".join(all_text)