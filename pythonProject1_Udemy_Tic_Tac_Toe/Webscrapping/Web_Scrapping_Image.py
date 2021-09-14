import requests
import lxml
import bs4

response = requests.get("https://en.wikipedia.org/wiki/Mahatma_Gandhi")
soup = bs4.BeautifulSoup(response.text, 'lxml')
# Select the image class and get the 8th image
image = soup.select(".thumbimage")[8]

# as image object is a Tag element object(dictionary)
# access the scr key and get the value(link) to the image
image_link = image['src']
print(image_link)

# let's make a new request to get the image only
res = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Gandhi_spinning.jpg/220px-Gandhi_spinning.jpg")
# for images we need content
# print(res.content)
# it is an binary file
image_link_content = res.content

# lets store it to a folder
f = open("Gandhi_spinning.jpg", 'wb')
f.write(image_link_content)
f.close()
