import d1p1 as prev

listsecondanswer = []

#how often does each number from list1 exist in list2?

total = 0

for index, item in enumerate(prev.list1):
    if prev.list2.count(item)>0:
        listsecondanswer.append([item, prev.list2.count(item)])

for i in range(len(listsecondanswer)):
    total = total + (float(listsecondanswer[i][0])*float(listsecondanswer[i][1]))

print(total)