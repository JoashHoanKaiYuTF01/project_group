from pathlib import Path
import csv   #import file 

# create file_path to csv files
file_path = Path.cwd()/"csv_reports"/"Profits and Loss.csv"

with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header
    # empty list to store profit transactions
    profit = []
    values = []

    # filter out only day and profit values
    for row in reader:
        profit.append([row[0], row[4]])


#creates function
def profit_and_loss():
    """
    function flags out days with profit deficit and corresponding deficit values   
    function writes the profit deficit details to a summary report .txt file
    """

    # create file path to summary_report.txt
    fp = Path.cwd()/"summary_report.txt"
    with fp.open(mode = "a") as file:
        
        # create a variable for counter
        counter = 0
        # use a global keyword to tweak profit and values variables not in the function
        global profit, values

        # assign first profit figure to a variable    
        prev_figure = profit[0][1]

        
        # for loop to calculate the difference in profit transactions
        for value in profit:

            # equation to find profit difference between different days
            profit_difference = float(value[1]) - float(prev_figure[1])

            # empty list to append profit deficit day and corresponding amount
            list1 = []
            # if statement loop with condition that profit difference is negative
            if profit_difference < 0:
                
                # append profit deficit day and corresponding amount to empty list
                list1.append(f"[PROFIT DEFICIT] DAY: {value[0]},  AMOUNT: HKD{abs(profit_difference)}")
            # else statement if "profit_difference" does not meet condition
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

1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
90

1
2
3
5
6
7
8
9
0
9
78
7
6
5
4
3
23
1
1
2
3
4
5
6
7
8
9
0








