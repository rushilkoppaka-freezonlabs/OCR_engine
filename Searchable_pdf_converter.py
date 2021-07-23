import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def img_to_searchablepdf(filename = 'table.jpg'):
    pdf = pytesseract.image_to_pdf_or_hocr(filename, extension='pdf')
    with open('test.pdf', 'w+b') as f:
        f.write(pdf)


