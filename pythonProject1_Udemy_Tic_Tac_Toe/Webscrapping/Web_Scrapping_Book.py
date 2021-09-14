import requests
import bs4

# Need to scrap all the books title which has Two start rating
for n in range(1, 51):
    base_url = 'https://books.toscrape.com/catalogue/page-{}.html'.format(n)
    res = requests.get(base_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # books in each page. we select product_pod class because we need to get the title of 2 star rating book
    products = soup.select(".product_pod")
    # print(products)
    # if the book is a 2 start rating book, then it will not return an empty list
    for product in products:
        prod_rating = product.select('.star-rating.Two')
        # print(prod_rating)
        if len(prod_rating) != 0:
            # select the anchor tag which contains the book title which returns a list
            prod_anchor_tag = product.select('a')
            # select the 2nd element of the list as it contains the title
            book = prod_anchor_tag[1]
            # select the title key so that we can get the value(name of that book)
            book_title = book['title']
            print(book_title)








