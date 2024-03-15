import fitz

def convert_pdf_to_text(pdf_file, text_file):
    pdf_document = fitz.open(pdf_file)

    text = ""

    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    with open(text_file, "w") as file:
        file.write(text)

pdf_file = 'dummy.pdf'

text_file = 'output_text_file.txt'

convert_pdf_to_text(pdf_file, text_file)

print("PDF converted to text successfully.")
