from PIL import Image
table = Image.open('word_matrix.png')
print(table.size)
new_mask = Image.open('mask.png')
updated_mask = new_mask.resize((1015, 559))
# print(updated_mask.show())

# lets mask the updated_mask on the table
table.putalpha(128)
# print(table.show())
updated_mask.putalpha(128)
table.paste(im=updated_mask, box=(0, 0), mask=updated_mask)
print(table.show())
