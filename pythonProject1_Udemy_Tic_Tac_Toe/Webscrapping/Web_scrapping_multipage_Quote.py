import requests
import bs4

#
page_continue = True
n = 1
# Instead of list we can use set() which store unique value
# set.add()
new_author_list = []
while page_continue:
    base_url = 'https://quotes.toscrape.com/page/{}/'.format(n)
    response = requests.get(base_url)
    soup = bs4.BeautifulSoup(response.text, 'lxml')

    # lets find unique author
    authors = soup.select(".author")
    for author in authors:
        if author.text in new_author_list:
            continue
        else:
            new_author_list.append(author.text)

    # Lets find the last page or not
    last_page = soup.select(".col-md-8")
    example = last_page[1]
    # print(type(example.text))
    if 'No quotes found!' in example.text:
        page_continue = False
        print("Page End")
    else:
        n += 1
        print("Page:", n)

print(new_author_list)
print(len(new_author_list))

