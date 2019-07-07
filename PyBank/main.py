import os
import csv

csvpath = os.path.join ('Pybank', 'Resources', 'budget_data.csv')
with open (budget_data.csv, newline="") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    #read first row as header.
    csv_header = next(csvfile)

budget_data = ['date', 'profit/loss']
#print total number of months
total_number_of_months = count(range(2, 88))
print(total_number_of_months)
#print net total of Profit/Loss
net_total = sum(range(3,88)
print(net_total)


#print average of the changes in Profit/Losses over total period
for 
#greatest increase in profits over entire period. need loop.
if 
#for x in 
#greatest decrease in profits (date and amount) over entire period- first loop inverted.
