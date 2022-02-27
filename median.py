import csv
with open('SOCR-HeightWeight.csv', newline = '') as median:
    reader = csv.reader(median)
    fileData = list(reader)

fileData.pop(0)
newData=[]

for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append(float(num))

lenData=len(newData)
newData.sort()
if lenData%2 == 0:
    m1 = float(newData[lenData//2])
    m2 = float(newData[lenData//2-1])
    m = (m1+m2)/2
else:
    m = newData[lenData//2]

print(m)
