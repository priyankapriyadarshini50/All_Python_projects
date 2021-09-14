from PIL import Image
# Open a image file
mac = Image.open('example.jpg')
# print(mac.show())
print(mac.size)
print(mac.filename)
print(mac.format_description)

# Crop the image with tuple argument(x, y, w, h)
cropped = mac.crop((0, 0, 600, 800))
# print(cropped.show())
# lets crop the computer from the example image with size(1993, 1257)
half = 1993/2
x = half - 200
w = half + 200
y = 800
h = 1257
mac_cropped = mac.crop((x, y, w, h))
# print(mac_cropped.show())

# paste the cropped pic on the original example.jpg
mac.paste(im=mac_cropped, box=(0, 0))
# print(mac.show())

# resize the image
# print(mac.resize((800, 800)).show())
# rotate the image
# print(mac.rotate(90).show())

# let's check color transparency
red = Image.open('red_color.jpg')
#print(red.show())
red.putalpha(128)
print(red.show()) # it looks pinkish



