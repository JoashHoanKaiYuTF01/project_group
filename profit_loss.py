from pathlib import Path
import csv   #import file 

file_path = Path.cwd()/"Profits and Loss.csv"

with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header
    profit = []
    values = []
    for row in reader:
        profit.append([row[0], row[4]])


#creates function
def profit_and_loss():
    """
    -    
    """
    fp = Path.cwd()/"summary_report.txt"
    with fp.open(mode = "a") as file:
        counter = 0
        global profit, values, deficits

    # create 2 empty lists to store profits with their corresponding days
    #profit = []
    #alues = []
    # create a file path using current working directory to link to csv file
    #file_path = Path.cwd()/"Profits and Loss.csv" 
    
    
    #with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        #reader = csv.reader(file)
        #next(reader) # skip header
    #create a file_path
    #with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    #    reader = csv.reader(file)
    #    next(reader) # skip header
        
         # append days and corresponding profits to empty list profit = [] 
        #for row in reader:
            #profit.append([row[0], row[4]])
            
        prev_figure = profit[0][1]

        #counter = 0

        for value in profit:

            profit_difference = float(value[1]) - float(prev_figure[1])
            list1 = []
            if profit_difference < 0:

                list1.append(f"[Profit Deficit] Day: {value[0]}  Amount: {profit_difference}")

            else:
                counter +=1       
                if counter == 11: 
                        
                    list1 = ["[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"]
                    return(list1)
            prev_figure = value  
            
            for i in list1:
                file.writelines(f"{i}\n")

#profit_and_loss()








