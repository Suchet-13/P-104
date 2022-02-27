import csv
from collections import Counter
with open('SOCR-HeightWeight.csv', newline = '') as mode:
    reader = csv.reader(mode)
    fileData = list(reader)

fileData.pop(0)
newData=[]

for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))

CounterData = Counter(newData)
range = {"50-60":0,"60-70":0,"70-80":0}

for height, occurence in CounterData.items():
    if 50<float(height)<60:
        range["50-60"] += occurence
    elif 60<float(height)<70:
        range["60-70"] += occurence
    elif 70<float(height)<80:
        range["70-80"] += occurence

modeRange,modeOccurence = 0,0

for rang,occurence in range.items():
    if occurence > modeOccurence:
        modeRange, modeOccurence = [int(range.split("-")[0]),int(range.split("-")[1])], occurence

m = float((modeRange[0]+modeRange[1])/2)
print(m)