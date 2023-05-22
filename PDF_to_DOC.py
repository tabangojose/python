import PyPDF2
from docx import Document

# Abrir el archivo PDF
pdf_file = open('/Users/josetabango/Downloads/CV Jose Enrique Tabango Castillo ES.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Crear un nuevo documento de Word
docx_file = Document()

# Recorrer todas las páginas del PDF y agregar su contenido al documento de Word
for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    text = page.extractText()
    docx_file.add_paragraph(text)

# Guardar el archivo de Word
docx_file.save('archivo.docx')
