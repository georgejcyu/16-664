import os
import csv
import numpy as np

with open('out.txt') as f:
    lines = f.readlines()


# print(lines[10][0])

header = ['guid/image','label']
test_list = os.listdir('test')
test_list.remove('.DS_Store')

img_list = []

for guid in test_list:
    guid_list =  os.listdir('test/' + guid)

    # Just get first 4 numbers
    new_list = []
    for name in guid_list:
        new_list.append(name[0:4])

    # Remove dups
    new_list = list(dict.fromkeys(new_list))

    for img in new_list:
        img_list.append(guid + '/' + img)

img_list.sort()
# open the file in the write mode
with open('submission.csv', 'w', newline="") as f:
    # create the csv writer
    writer = csv.writer(f, delimiter=",")

    # write a header to the csv file
    writer.writerow(header)

    # write data
    for i in range(2631):
        writer.writerow([img_list[i],lines[i][0]])