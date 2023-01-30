from pathlib import Path
import csv

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

        for row in reader:
            cash_on_hand.append([row[0], row[1]])

        for i in range(len(cash_on_hand)):
            COH_values.append([cash_on_hand[i][0], float(cash_on_hand[i][1]) - float(cash_on_hand[i-1][1])])

        COH_values[0][-1] = 0

        for deficits in COH_values:
            if deficits[1] < 0: # i[1] is the change in profit, the second column in the table
                
                if len(deficits) > 0:
                    # ensure that function will return multiple days of cash deficit if applicable
                    for i in range(len(deficits)):
                         return f"[Cash on Hand Deficit] Day: {deficits[0]}, Amount: {deficits[1]}"
                else:
                    return ("cash surplus! well done!")

print(COH())


print("hello tessa")
print("hello dave can u see this message?")

print("hi davey")

print("hi amelda")
print("hi amelda")
print("hi tessa")








