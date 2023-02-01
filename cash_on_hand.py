from pathlib import Path   #imports path 
import csv    #imports file 

#creates a function 
def COH(): 
    # create empty lists to append cash on hand and corresponding days from csv
    global COH_values, cash_on_hand, deficits
    #create empty list to append values into it ##
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

        #print(cash_on_hand)
        #reiterate the function
        #for i in range(len(cash_on_hand)):
            #COH_values.append([cash_on_hand[i][0], (float(cash_on_hand [i][1]) - float(cash_on_hand[i-1][1]))])

        #COH_values[0][-1] = 0

        #print(COH_values)
        counter = 0
        prev_figure = cash_on_hand[counter][1]

        #print(cash_on_hand)
        flag_list = []
        #for loop to iterate over each value 
        for value in cash_on_hand:
                
                
            #print(value)
            #print(value[1])
                cash_difference = float(value[1])-float(prev_figure)
                #print(cash_difference)

                if cash_difference < 0:
                    flag_list.append(cash_difference)
            
                counter += 1
                    
                #print(flag_list)   
            #elif cash_difference >= 0:
                #print("cash surplus")
        
        
        #print(cash_on_hand)
        #print(cash_on_hand[0][1])
        #print(value)
        #print(value[1])
        print(flag_list)






        #deficits = 0
        #day = 0

        #list1 = []
        #for i in COH_values:
            #if i[1]<0:
                #day = i[0]
                #deficits = i[1]
                
                #day.append(i[0])
                #deficits.append(i[1])
        #print(deficits)
        #print(day)
                #list1 = list1.append(f"[Cash on Hand Deficit] Day: {day}, Amount: {deficits}")
                #return list1
          
            

        #print(COH_values)
        #print(cash_on_hand)

        #for loop ot iterate over each value 
        for deficits in COH_values:
            
                #print(deficits)
                if deficits[1] < 0: # i[1] is the change in profit, the second column in the table
                
                    if len(deficits) > 0:
                    # ensure that function will return multiple days of cash deficit if applicable
                        for i in range(len(deficits)):
                            print(f"[Cash on Hand Deficit] Day: {deficits[0]}, Amount: {deficits[1]}")
                     
                    else:
                        print("[CASH SURPLUS] Well done!")
                
        

                
#executes function
COH()


















