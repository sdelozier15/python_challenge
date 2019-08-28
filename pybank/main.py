import csv
import os

budget_data = os.path.join('budget_data.csv')

def getthestuff(budget_data):
    
    months = 0
    total = 0
    maxrev = 0
    minrev = 0
    avgchange = 0
    maxmonth = ""
    minmonth = ""
    prev = 0
    delta = 0
    deltalist = []
    monthslist = []
    with open(budget_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        
        first_row = next(csvreader)
        months = 1
        total = total + int(first_row[1])
        prev = int(first_row[1])
        maxrev = int(first_row[1])
        minrev = int(first_row[1])
        
        for row in csvreader:
            months += 1
            total = total + int(row[1])

            delta = int(row[1]) - prev
            prev = int(row[1])
            deltalist = deltalist + [delta]
            monthslist = monthslist + [row[0]]
            
            
            current_month = row[0]
            pnl = int(row[1])
            avgchange = sum(deltalist)/ len(deltalist)
    
            if pnl > maxrev:
                maxrev = delta
                maxmonth = current_month
            if pnl < minrev:
                minrev = delta
                minmonth = current_month
        return [months, total, avgchange, maxrev, minrev, maxmonth, minmonth]
            
final = getthestuff(budget_data)
print(final)

print("Financial analysis")
print("_______________________________")
print(f"Total months: {(final[0])}")
print(f"Total: ${(final[1])}")
print(f"Average Change: {(final[2])}")
print(f"Greatest Increase in Profits: {(final[5])} (${(final[3])})")
print(f"Greatest Decrease in Profits: {(final[6])} (${(final[4])})")
