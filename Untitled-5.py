tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]

maxLengthList = []
for l in tableData:
    a = 0
    for s in l:
        if len(s) > a:
            a = len(s)
    maxLengthList.append(a)

for i in range(len(tableData[0])):
    t = ""
    for l in range(len(tableData)):
        content = tableData[l]
        content = content[i]
        if l == 0:
            t += content.rjust(maxLengthList[l])
        else:
            t += content.ljust(maxLengthList[l])
        t += " "
    print(t)


