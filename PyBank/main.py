#import modules
import csv
import os

#create path to csv file
pybank = os.path.join('Resources', 'budget_data.csv')

#open csvfile
with open(pybank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #write out variables and list that I may need
    total_months = 0
    total_pnl = 0
    profit_loss_change = 0
    i = 0
    total_profit_loss = 0
    count_profitloss = 0

    maxpl = [float ('-inf'), 0]
    minpl = [float ('inf'), 0]
    months = []
    profit_loss_list = []
    profit_loss = []
    date = []
    profit_loss_change_list = []

    for row in csvreader:
        months.append(row[0])
        profit_loss = int(row[1])
        date = str(row[0])
        
        total_months = len(months)

        if len(profit_loss_list)!= 0:
            profit_loss_change = profit_loss - profit_loss_list[i]
            i += 1
            if maxpl[0] < profit_loss_change:
                maxpl = [profit_loss_change, date]
            if minpl[0] > profit_loss_change:
                minpl = [profit_loss_change, date]
            profit_loss_change_list.append(profit_loss_change)
            count_profitloss = len(profit_loss_change_list)
            #print(date, profit_loss_change)

        profit_loss_list.append(profit_loss)
        total_change = sum(profit_loss_list)
        total_profit_loss = sum(profit_loss_change_list)
        
        #print(date, profit_loss_change)
        #high_value = max(profit_loss_change_list)

    avg_change = total_profit_loss/count_profitloss
    high_change = max(profit_loss_change_list)
    low_change = min(profit_loss_change_list)    
    
    # #print to validate that the numbers match
    # print(total_months)
    # print(total_change)
    # print(total_profit_loss)
    # print(avg_change)
    # print(count_profitloss)
    # print(high_change)
    # print(low_change)
    # print(maxpl)
    # print(minpl)

    #print statement for election results
    print("Financial Analysis")
    print("---------------------------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + str(total_change))
    print("Average Change: " + str(avg_change))
    print("Greatest Increase in Profits: " + str(high_change))
    print("Greatest Decrease in Profits: " + str(low_change))

with open('analysis/Financial_Analysis.txt','w') as text:
    text.write("Financial Analysis\n")
    text.write("---------------------------------------\n")
    text.write("Total Months: " + str(total_months) + "\n")
    text.write("Total: " + str(total_change) + "\n")
    text.write("Average Change: " + str(avg_change) + "\n")
    text.write("Greatest Increase in Profits: " + str(high_change) + "\n")
    text.write("Greatest Decrease in Profits: " + str(low_change) +"\n")