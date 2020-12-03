import csv
import re
data = []

myCardData = {}
myCardDataTotal = {}

with open('customerData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

for item in data:
    thisCard = item['Credit Card']
    thisSpend = float(item['Spent Past 12 Months'].strip('$'))

    if thisCard in myCardData:
        myCardData[thisCard] = myCardData[thisCard] + 1
        myCardDataTotal[thisCard] = myCardDataTotal[thisCard] + thisSpend
    else:
        myCardData[thisCard] = 1
        myCardDataTotal[thisCard] = thisSpend

for item in myCardData:
    myAvg = float(myCardDataTotal[item] / float(myCardData[item]))
    print(str(item) + " " + str(myCardData[item]) + " " + str(myCardDataTotal[item]))
    print(myAvg)
