import os
import csv

pybank= os.path.join('/users/rheapius/python_challenge/pybank/resources/budget_data.csv')

#variables for storing data from rows
months=[]
Profits=[]

#setting function for sum of  profits
def sum(lst):
    total=0
    for number in lst:
        total += int(number)
    return total

with open(pybank, 'r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    header= next(csvreader)
    for row in csvreader:
        months.append(row[0])
        Profits.append(row[1])

#assigning formulas for output

    total_months= int(len(months))
    net_profit= int(sum(Profits))
    average= round(int(net_profit/total_months))

    Greatest_increase= int(max(Profits))
    Greatest_decrease= int(min(Profits))
    
    Output= (
        f"Financial Analysis\n"
        f"------------------------------------------------------\n"   
        f"Total Months: {total_months}\n"
        f"Total: $ {net_profit}\n"
        f"Average Change:$ {average}\n"
        f"Greatest increase in profits: $ ({Greatest_increase})\n"
        f"Greatest decrease in profits: $ ({Greatest_decrease})\n"
        )
print (Output)

#exporting to text file

results= os.path.join('/users/rheapius/python_challenge/pybank/analysis/results.txt')

with open(results, "w") as text_file:
    text_file.write(Output)




    
        
                                          




















