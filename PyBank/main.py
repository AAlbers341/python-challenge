# Import Module for to create a file path across opertaing systems
import os 

# Import Module for reading CSV files
import csv

cmpy_budget_data = os.path.join('Resources', 'budget_data.csv')

#Lists to store csv budget data
months = []
total_profit_and_loss = []


with open(cmpy_budget_data) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first 
    csv_header = next(csvreader)


    for row in csvreader:

        #Total number of months in dataset
        months.append(row[0])

        #Total profit and loss of company append to total_profit_and_loss list
        total_profit_and_loss.append(int(row[1]))

# Period profit and loss variances 
period_variance = [total_profit_and_loss[row + 1] - total_profit_and_loss[row] for row in range(len(total_profit_and_loss) - 1)]

# Average profit and loss variances in budget dataset 
def average(period_variance):
    length = len(period_variance)
    total = 0.0
    for variance in period_variance:
        total += variance
    return total / length

# Identifying greatest increase and decrease indexes in period variance
max_profits_index = period_variance.index(max(period_variance))
min_profits_index = period_variance.index(min(period_variance))

# From greatest increase and decrease indexes above, looping through period month list to identify the month the variance took place
for month in range(len(months)):
    if month == max_profits_index:
        max_profit_month = months[month + 1]
    elif month == min_profits_index:
        min_profit_month = months[month + 1]


print(" ")
print("Financial Analysis")
print(" ")
print("-----------------------------")
print(" ")
print(f"Total Months: {len(months)}")
print(" ")
print(f"Total: ${sum(total_profit_and_loss)}")
print(" ")
print(f"Average Change: ${round(average(period_variance),2)}")
print(" ")
print(f"Greatest Increase in Profits: {max_profit_month} (${max(period_variance)}) ")
print(" ")
print(f"Greatest Decrease in Profits: {min_profit_month} (${min(period_variance)}) ")
print(" ")


# Set variable for output file
output_file = os.path.join("analysis", "cmpy_budget_data.txt")


with open(output_file, 'w') as file:
    # Redirect the standard output to the file
    import sys
    original_stdout = sys.stdout
    sys.stdout = file

    print(" ")
    print("Financial Analysis")
    print(" ")
    print("-----------------------------")
    print(" ")
    print(f"Total Months: {len(months)}")
    print(" ")
    print(f"Total: ${sum(total_profit_and_loss)}")
    print(" ")
    print(f"Average Change: ${round(average(period_variance),2)}")
    print(" ")
    print(f"Greatest Increase in Profits: {max_profit_month} (${max(period_variance)}) ")
    print(" ")
    print(f"Greatest Decrease in Profits: {min_profit_month} (${min(period_variance)}) ")
    print(" ")

    # Restore the standard output
    sys.stdout = sys.__stdout__
