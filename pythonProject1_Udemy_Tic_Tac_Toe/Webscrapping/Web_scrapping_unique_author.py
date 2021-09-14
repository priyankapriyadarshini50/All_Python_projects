import requests
import bs4

response = requests.get("https://quotes.toscrape.com/page/9/")
soup = bs4.BeautifulSoup(response.text, 'lxml')
authors = soup.select('.author')
new_author_list = []
for author in authors:
    print(author.text)
    if author.text in new_author_list:
        continue
    else:
        new_author_list.append(author.text)
print(new_author_list)

