from pathlib import Path   #imports path 
import csv     #import file 


#creates a file_path
file_path = Path.cwd()/"Cash on Hand.csv" 

    
    # open csv file and read it
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header
    cash_on_hand = []
    for row in reader:
        cash_on_hand.append([row[0], row[1]])

#counter = 0 
#creates a function 
def COH():
    fp = Path.cwd()/"summary_report.txt"
    with fp.open(mode = "a") as file: 
    # create empty lists to append cash on hand and corresponding days from csv
        counter = 0 
        global cash_on_hand, value, cash_difference
    
        prev_figure = cash_on_hand[0][1]
    
        
        for value in cash_on_hand:
                
                cash_difference = float(value[1])-float(prev_figure[1])
                
                list = []

                if cash_difference < 0:
                    list.append(f"[Cash Deficit] DAY: {value[0]}  AMOUNT: HKD{abs(cash_difference)}")
                    #print(list)
                else:
                    counter +=1       
                    if counter == 11: 
                        list = ["[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"]
                        return(list)
                prev_figure = value

                for i in list:
                    file.writelines(f"{i}\n")
                
             
#executes function
COH()



    








