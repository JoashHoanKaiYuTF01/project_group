from pathlib import Path
import csv   #import file 

# create file_path to csv files
file_path = Path.cwd()/"csv_reports"/"Profits and Loss.csv"

with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header
    profit = []
    values = []

    # filter out only day and profit values
    for row in reader:
        profit.append([row[0], row[4]])


#creates function
def profit_and_loss():
    """
    -    
    """

    # create file path to summary_report.txt
    fp = Path.cwd()/"summary_report.txt"
    with fp.open(mode = "a") as file:
        
        counter = 0
        global profit, values, deficits

        # assign first profit figure to a variable    
        prev_figure = profit[0][1]

        

        for value in profit:

            # equation to find profit difference between different days
            profit_difference = float(value[1]) - float(prev_figure[1])

            # empty list to append profit deficit day and corresponding amount
            list1 = []

            if profit_difference < 0:
                
                # append profit deficit day and corresponding amount to empty list
                list1.append(f"[Profit Deficit] Day: {value[0]}  Amount: HKD{abs(profit_difference)}")

            else:
                counter +=1       
                if counter == 11: 
                        
                    list1 = ["[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"]
                    return(list1)
            # to ensure that profit value iterates through the list of profit values   
            prev_figure = value  
            
            # write profit deficits to summary_report.txt
            for i in list1:
                file.writelines(f"{i}\n")









