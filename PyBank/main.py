import os
import csv

pybank= os.path.join('/users/rheapius/python_challenge/pybank/resources/budget_data.csv')

months=[]
ProfitLoss=[]

with open(pybank, 'r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    header= next(csvreader)
    for range in csvreader:
        months.append(range[0])
        ProfitLoss.append(range[1])
        
        total_months= int(len(months))
        total= int(float(sum(ProfitLoss)))
        average= round(int(float(total/total_months)))

        Greatest_increase= int(float(max(ProfitLoss)))

        Greatest_decrease= int(float(min(ProfitLoss)))

        print(f"------------------------------------------------------")
        print(f"Total Months: {str(total_months)}")
        print(f"Total: {str(total)}")
        print(f"Average Change:{str(average)}")
        print(f"Greatest increase in profits: $ {str(Greatest_increase)}")
        print(f"Greatest decrease in profits: {str(Greatest_decrease)}")
                                          




















