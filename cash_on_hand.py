from pathlib import Path   #imports path 
import csv     #import file 


#creates a file_path to csv file
file_path = Path.cwd()/"csv_reports"/"Cash on Hand.csv" 

    
# open csv file and read it
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header
    cash_on_hand = []
    for row in reader:
        cash_on_hand.append([row[0], row[1]])


#creates a function 
def COH():
    # create and open .txt file for writing summary_report
    fp = Path.cwd()/"summary_report.txt"
    with fp.open(mode = "a") as file: 
    # create empty lists to append cash on hand and corresponding days from csv
        counter = 0 
        global cash_on_hand, value, cash_difference
        # assign first cash on hand figure to a variable
        prev_figure = cash_on_hand[0][1]
    
        
        for value in cash_on_hand:
                
                # equation to find cash on hand difference between different days
                cash_difference = float(value[1])-float(prev_figure[1])
                
                # empty list to append cash deficit day and corresponding amount
                list = []

                if cash_difference < 0:

                    # append cash deficit day and corresponding account to empty list
                    list.append(f"[Cash Deficit] DAY: {value[0]}  AMOUNT: HKD{abs(cash_difference)}")
                    #print(list)
                else:
                    counter +=1       
                    if counter == 11: 
                        list = ["[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"]
                        return(list)
                # to ensure that cash on hand value moves through the list of cash on hand values
                prev_figure = value

                # write cash on hand deficits to summary_report.txt
                for i in list:
                    file.writelines(f"{i}\n")
                
             





    








