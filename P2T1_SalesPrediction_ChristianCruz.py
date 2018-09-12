#This program gets the annual profit by multiplying 23% times the total sales
#9/12/2018
#CTI-110 P2T1 - Sales Prediction
#Christian Cruz
#

#Get the projected sales total
totalSales = float(input('Enter the projected sales: '))

#Calculate the profit as 23 percent of total sales
profit = totalSales * 0.23

#Display the profit
print('The profit is $', format(profit,',.2f'))

                   
