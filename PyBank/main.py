# import the magic ...

import os
import csv

# I didn't know if I was allow to import this package but here it is... (I thought, well, it isn't Pandas so let's go for it...)
from statistics import mean

# Create the space (lists) to put our data

total_number_of_months = []
total_profit_losses = []
total_change = []

# "Call" the data... as the budget data document is in the Resources file (which is under the same PyBank file as this main.py document), I don't include the ".."

budget = os.path.join('Resources', 'budget_data.csv')

#read the data taking the first record as a header and then going through each row. Stating that after the "," it continues reading on the line below
with open(budget) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

#1: Loop through each of the values. 2: Then add each one to the list which was created above

    for i in csvreader:
        total_number_of_months.append(i[0])
        total_profit_losses.append(int(i[1]))

# Here is a similar process - In each of the profit/losses, we compare it to the previous one to see the difference
    for j in range(len(total_profit_losses)-1):
        total_change.append(total_profit_losses[j+1]- total_profit_losses[j])
                      
# Pretty simple - min, max and mean of the values in total_change - then we get the min and max profit/loss change by indexing the newly created list (total_change)

greatest_increase = max(total_change)
greatest_decrease = min(total_change)
average = mean(total_change) 

month_greatest_increase = total_change.index(greatest_increase)
month_greatest_decrease = total_change.index(greatest_decrease)

# Then we print the results and try to match the given format

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {len(total_number_of_months)}")
print(f"Total: ${sum(total_profit_losses)}")
print(f"Average Change: ${round(average,3)}")
print(f"Greatest Increase in Profits: {total_number_of_months[month_greatest_increase]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {total_number_of_months[month_greatest_decrease ]} (${(str(greatest_decrease))})")   


# Finally we create the .txt document with the print part from above
output = os.path.join("analysis", "output.txt")

with open(output,"w") as result:
    result.write("Financial Analysis")
    result.write("\n")
    result.write("--------------------")
    result.write("\n")
    result.write(f"Total Months:{len(total_number_of_months)}")
    result.write("\n")
    result.write(f"Total: ${sum(total_profit_losses)}")
    result.write("\n")
    result.write(f"Average Change: ${round(average,3)}")
    result.write("\n")
    result.write(f"Greatest Increase in Profits: {total_number_of_months[month_greatest_increase]} (${(str(greatest_increase))})")
    result.write("\n")
    result.write(f"Greatest Decrease in Profits: {total_number_of_months[month_greatest_decrease ]} (${(str(greatest_decrease))})")



