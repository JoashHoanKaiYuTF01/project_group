from pathlib import Path
import csv

def profit_and_loss():
    """
    
    """
    global profit, values, deficits

    # create 2 empty lists to store profits with their corresponding days
    profit = []
    values = []
    # create a file path using current working directory to link to csv file
    file_path = Path.cwd()/"Profits and Loss.csv" 
    
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header
        
         # append days and corresponding profits to empty list profit = [] 
        for row in reader:
            profit.append([row[0], row[4]])
        
        # access individual transactions in each row of the table 
        for i in range(len(profit)): # for each row in the table

            # append profit and profit change for each day to empty list
            values.append([profit[i][0], (int(profit[i][1]) - int(profit[i-1][1]))])
        
        # remove the profit difference for Day 30
        values[0][-1] = 0
      
        #deficits = [i for i in values if i[1]<0]
        #print(deficits)
        for deficits in values:
            if deficits[1] < 0: # i[1] is the change in profit, the second column in the table
                
                if len(deficits) > 0:
                    # ensure that function will return multiple days of cash deficit if applicable
                    for i in range(len(deficits)):
                         return f"[Profit Deficit] Day: {deficits[0]}, Amount: {deficits[1]}"
                else:
                    return ("Profit increase! well done!")
# execute function
print(profit_and_loss())










