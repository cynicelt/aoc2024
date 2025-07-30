import csv
import pandas as pd


#declare the lists
list1 = []
list2 = []
listresult = []

# Open the CSV file
with open('data/d1_input.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

for item in data:
    list1.append(item[0].split()[0])
    list2.append(item[0].split()[1])

#sort the lists
list1.sort()
list2.sort()

for index, item in enumerate(list1):
    listresult.append(abs(float(list1[index])-float(list2[index])))

print(sum(listresult))








