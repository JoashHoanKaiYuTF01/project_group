from pathlib import Path   #imports path 
import csv

#creates a function 
def COH(): 
    # create empty lists to append cash on hand and corresponding days from csv
    global cash_on_hand
    cash_on_hand = []
    
    # create a file path using current working directory to link to csv file
    file_path = Path.cwd()/"Cash on Hand.csv" 
    
    # open csv file and read it
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        
        #for loop that iterates over each value until a criteria is met
        for row in reader:
            cash_on_hand.append([row[0], row[1]])

        
        prev_figure = cash_on_hand[0][1]

        counter = 0
        
        for value in cash_on_hand:
                
                cash_difference = float(value[1])-float(prev_figure[1])
                #print(cash_difference)

                if cash_difference < 0:
                    #flag_list.append(cash_difference)
                    print(f"[Cash Deficit] Day: {value[0]}  Amount: {cash_difference}")
                
                else:
                    counter +=1       
                    if counter == 11: 
                        return f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
                prev_figure = value  
             
#executes function
COH()


















