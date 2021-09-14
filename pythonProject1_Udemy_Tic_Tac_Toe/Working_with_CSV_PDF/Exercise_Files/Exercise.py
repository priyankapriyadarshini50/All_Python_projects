import csv

data = open("find_the_link.csv", encoding='utf-8')
# convert to csv data
data_csv = csv.reader(data)
# convert it a list of list
data_lines = list(data_csv)
print(len(data_lines))
new_line = ''
for i in range(0, len(data_lines)):
    # print(data_lines[i][i])
    new_line += data_lines[i][i]

print(new_line)
# Task2
import PyPDF2
import re

f = open('Find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)

for i in range(0, pdf_reader.numPages):
    print(i)
    page = pdf_reader.getPage(i)
    page_text = page.extractText()

    # pattern = r'\d{3}.\d{3}.\d{4}'
    # Initially we do not know the pattern of the phone number, to fine that we just apply \d{3}
    pattern = r'\d{3}'
    # if we search it will return thr 1st occurrence, we use finditer
    # match = re.finditer(pattern, page_text)
    for match in re.finditer(pattern, page_text):
        print(match)
        # print(page_text[1727: 1738+20])
# got the number in page 13
res_page = pdf_reader.getPage(13)
res_page_text = res_page.extractText()
print("The result phone number:", res_page_text[1727: 1738+3])

