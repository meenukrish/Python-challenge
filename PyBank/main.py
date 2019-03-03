import os
import csv


Totalmonths = 0 
Total = 0
PLPreviousrow = 0
AverageChanges = 0.0
Changes = {}
GrProfitIncrease = 0
GrProfitDecrease = 0
GrProfitIncMonth =""
GrProfitDecMonth =""


csvpath = os.path.join("resources","budget_data.csv")

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
   
    for row in csvreader:
        Totalmonths +=1
        Total = Total + (int(row[1]))
        if (PLPreviousrow != 0):
            Changes[row[0]]= int(row[1])-PLPreviousrow   # Insert the Change month and the value in a Dictionary
        PLPreviousrow = int(row[1])

    for month , changevalue in Changes.items():
        AverageChanges += changevalue

        if changevalue > GrProfitIncrease:
            GrProfitIncrease = changevalue
            GrProfitIncMonth = month
        
        if changevalue < GrProfitDecrease:
            GrProfitDecrease = changevalue
            GrProfitDecMonth = month
            
print("Financial Analysis")
print("===================")
print(f"Total Months: {Totalmonths}")
print(f"Total : $ {Total}")
print(f"Average Changes : $ {AverageChanges}")
print(f"Greatest Increase in Profits:{GrProfitIncMonth} ($ {GrProfitIncrease})")
print(f"Greatest Increase in Profits:{GrProfitDecMonth} ($ {GrProfitDecrease})")


output_path = os.path.join("output", "Financial Analysis.txt")

with open(output_path, 'w', newline="\n") as txtFile:

      print("Financial Analysis" , end ='\n', file = txtFile)
      print("===================" ,end ='\n', file = txtFile)
      print(f"Total Months: {Totalmonths}", end ='\n', file=txtFile)
      print(f"Total : $ {Total}" , end='\n', file=txtFile)
      print(f"Average Changes : $ {AverageChanges}" , end='\n' , file=txtFile)
      print(f"Greatest Increase in Profits:{GrProfitIncMonth} ($ {GrProfitIncrease})", end='\n' , file=txtFile)
      print(f"Greatest Increase in Profits:{GrProfitDecMonth} ($ {GrProfitDecrease})" , end ='\n' , file=txtFile)


    