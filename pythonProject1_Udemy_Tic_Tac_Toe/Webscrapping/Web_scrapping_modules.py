import requests
import lxml
import bs4
# GRABBING A TITLE AND PARAGRAPHS
#res = requests.get("https://example.com/")
#print(type(res))
#web_text = res.text
# print(web_text)

# Create a soup object and lxml is the parser
#soup = bs4.BeautifulSoup(web_text, "lxml")
#print(soup.select('title'))
#title_tag = soup.select('title')[0]
#print(title_tag)
#print(type(title_tag))
#print(title_tag.getText())
# lets fine the paragraph
#paragraphs = soup.select('p')
#print(paragraph)
#for paragraph in paragraphs:
    #print(paragraph.getText())

#print(paragraph[1])
#print(paragraph[1].getText())

# GRABBING THE CONTENTS OF TABLE
request = requests.get('https://en.wikipedia.org/wiki/Mahatma_Gandhi')
soup_ele = bs4.BeautifulSoup(request.text, "lxml")
table_data = soup_ele.select('.infobox-data')
for data in table_data:
    print(data.text)


