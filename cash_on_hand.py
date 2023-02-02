from pathlib import Path   #imports path 
import csv



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
    with fp.open(mode = "w") as file: 
    # create empty lists to append cash on hand and corresponding days from csv
        counter = 0 
        global cash_on_hand, value, cash_difference
    #cash_on_hand = []
        prev_figure = cash_on_hand[0][1]
    # create a file path using current working directory to link to csv file
    #file_path = Path.cwd()/"Cash on Hand.csv" 
    
    # open csv file and read it
    #with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        #reader = csv.reader(file)
        #next(reader) # skip header

        
        #for loop that iterates over each value until a criteria is met
    #for row in reader:
            #cash_on_hand.append([row[0], row[1]])

        
    #prev_figure = cash_on_hand[0][1]

    #counter = 0
        
        for value in cash_on_hand:
                
                cash_difference = float(value[1])-float(prev_figure[1])
                
                list = []

                if cash_difference < 0:
                    list.append(f"[Cash Deficit] DAY: {value[0]}  AMOUNT: HKD{abs(cash_difference)}")
                    print(list)
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

#cwd = Path.cwd()
##print(cwd)
#file_path = cwd/"summary_report.txt"
#file_path.touch()
##print(file_path)
##print(file_path.exists())
#
#file_path = Path.cwd()/"summary_report.txt"
#
#with file_path.open(mode = "w") as file:
#    if len(list) > 1:
#        for i in list:
#            file.writelines(f"{i}")
#    else:
#        file.writelines(list)
#print(cash_difference)
#print(value)
#











