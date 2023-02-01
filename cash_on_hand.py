from pathlib import Path   #imports path 
import csv    #imports file 

#creates a function 
def COH(): 
    # create empty lists to append cash on hand and corresponding days from csv
    global COH_values, cash_on_hand, deficits
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
        prev_figure = cash_on_hand[counter][1]

        #print(cash_on_hand)
        flag_list = []
        for value in cash_on_hand:
                
                cash_difference = float(value[1])-float(prev_figure[1])
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

        for deficits in COH_values:
            
                #print(deficits)
                if deficits[1] < 0: # i[1] is the change in profit, the second column in the table
                
                else:
                    counter +=1       
                    if counter == 11: 
                        return f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
                prev_figure = value  
             
#executes function
COH()


















