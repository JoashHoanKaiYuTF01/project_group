from pathlib import Path   #imports path 
import csv

#creates a function 
def COH(): 
    # create empty lists to append cash on hand and corresponding days from csv
    cash_on_hand = []
    COH_values = []

    # create a file path using current working directory to link to csv file
    file_path = Path.cwd()/"Cash on Hand.csv" 
    
    # open csv file and read it
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        #for loop that iterates over each value until a criteria is met
        for row in reader:
            cash_on_hand.append([row[0], row[1]])

        for i in range(len(cash_on_hand)):
            COH_values.append([cash_on_hand[i][0], (float(cash_on_hand[i][1]) - float(cash_on_hand[i-1][1]))])

        COH_values[0][-1] = 0

        for deficits in COH_values:
            if deficits[1] < 0: # i[1] is the change in profit, the second column in the table
                
                if len(deficits) > 0:
                    # ensure that function will return multiple days of cash deficit if applicable
                    for i in range(len(deficits)):
                         return f"[Cash on Hand Deficit] Day: {deficits[0]}, Amount: {deficits[1]}"
                else:
                    return ("cash surplus! well done!")
                
#executes function
print(COH()) 

from pathlib import Path
import csv

def profit_and_loss():
    global profit, values, deficits
    profit = []
    values = []
    current_dir = Path.cwd()/"Profits and Loss.csv" 
    
    with current_dir.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header
        
        for row in reader:
            profit.append([row[0], row[4]])
        
        for i in range(len(profit)): # for each row in the table
            #print(profit[i][0], (int(profit[i][1]) - int(profit[i-1][1])))
            values.append([profit[i][0], (int(profit[i][1]) - int(profit[i-1][1]))])
        
        values[0][-1] = 0
      
        deficits = [i for i in values if i[1]<0]
        print(deficits)
        
        if len(deficits )> 0:
            for i in range(len(deficits)):
                print(f"[cash deficit] day: {deficits[i][0]}, amount: {deficits[i][1]}")
        else:
            print("cash surplus! well done!")
        
        
        
profit_and_loss()

















