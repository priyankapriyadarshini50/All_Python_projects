import csv

# open the csv file
data = open('example.csv', mode='r', encoding='utf-8')
print(data)
# Convert to csv data
csv_data = csv.reader(data)
print(csv_data)
# Reformat it into a python object list of lists
csv_list = list(csv_data)
# print(csv_list)
# The 1st element is a list of column names
print(csv_list[0])

# I want to get first 15 email addresses
for element in csv_list[1:16]:
    print(element[3])

# get the full name of 1st 20 people in the csv file
for element in csv_list[1:20]:
    print(element[1] + ' ' + element[2])

# Write to a csv file
file_obj = open('my_csv_file.csv', mode='w')
# I want to insert full name and email address of top ten people
csv_writer_obj = csv.writer(file_obj, delimiter=';')
csv_writer_obj.writerow(['ID', 'Full_Name', 'Email'])

# Here element is each row in the original(example.csv) file
for element in csv_list[1:11]:
    csv_writer_obj.writerow([element[0], element[1] + ' ' + element[2], element[3]])


