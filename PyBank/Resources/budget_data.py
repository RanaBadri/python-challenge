import csv
import os

filename = "budget_data.py"
with open("budget_data.csv",'r') as myfile:
  myfile = csv.reader(myfile,delimiter=",")
  
  total = 0
  months = 0
  total_change = 0
  previous = 0
  change_values = []
  header = next(myfile)
  

  for row in myfile:
    total = total + float(row[1])
    months = months +1
    
    # find the change then the average
    change = float(row[1]) - previous
    if months >1 :
      
      total_change = total_change + change
    previous = float(row[1])
 
    
    
  #finding the greatest increase and decrease in Profit/Losses
    change_values.append(change)
    Greatest_Increase = min(change_values)
    Greatest_Decrease = max(change_values)

avg = total_change / (months - 1)
    
print(f"Total Profit_Losses is:{total} \nTotal Number of Months is: {months}")
print(f"\nAverage is: {round(avg,2)} \nGreates Increase is: {Greatest_Increase} \nGreatest Decrease is: {Greatest_Decrease}")

with open("output.txt", "w") as text_file:
    text_file.write(f"Total Profit_Losses is:{total} \nTotal Number of Months is: {months}")
    text_file.write(f" \nAverage is: {round(avg,2)} \nGreates Increase is: {Greatest_Increase} \nGreatest Decrease is: {Greatest_Decrease}")