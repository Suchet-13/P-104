import csv
with open('SOCR-HeightWeight.csv', newline = '') as mean:
    reader = csv.reader(mean)
    fileData = list(reader)

fileData.pop(0)
newData=[]

for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append(float(num))

lenData = len(newData)
total = 0

for a in newData:
    total += a

m = total/lenData
print(m)