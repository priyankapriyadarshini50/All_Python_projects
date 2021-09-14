# UDEMY HOME WORK
import requests
import bs4

response = requests.get("https://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(response.text, 'lxml')

# select all html tag
# content = soup.select('html')
# print(content)

# Select all the unique authors on the 1st page
# set always keep unique values
author_set = set()
authors = soup.select('.author')
# print(authors)
for author in authors:
    # print(author.text)
    author_set.add(author.text)


# print(author_list)
# print(set(author_list))

# Create a list of all quotes in the 1st page
quote_list = []
quotes = soup.select(".text")
for quote in quotes:
    # print(quote.text)
    quote_list.append(quote.text)
# print(quote_list)

# Find out the top ten tags
all_tags = soup.select('.tag-item')
print(all_tags)

for tag in all_tags:
    print(tag.text)


