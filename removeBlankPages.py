import PyPDF2

def remove_blank_pages(path_to_pdf):
    pdf_reader = PyPDF2.PdfFileReader(path_to_pdf)
    pdf_writer = PyPDF2.PdfFileWriter()
    
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        if page.extractText().strip():
            pdf_writer.addPage(page)
    
    new_pdf_path = "new_pdf_without_blank_pages.pdf"
    with open(new_pdf_path, 'wb') as f:
        pdf_writer.write(f)
    
    return new_pdf_path
