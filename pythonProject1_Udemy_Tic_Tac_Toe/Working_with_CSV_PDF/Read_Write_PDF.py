import PyPDF2

# Read a binary pdf file
# Open the file
file_obj = open('Working_Business_Proposal.pdf', mode='rb')
# Create a Reader object
pdf_reader = PyPDF2.PdfFileReader(file_obj)
print(pdf_reader)
print("Total number of pages in the pdf file:", pdf_reader.numPages)
# Grab the 1st page(which has index 0) and extract the text
page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
print(page_one_text)


# Copy the first page and add to another document
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page_one)
f1 = open('my_new_pdf.pdf', 'wb')
pdf_writer.write(f1)

file_obj.close()
f1.close()
