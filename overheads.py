from pathlib import Path  
import csv    #import file 


file_path= Path.cwd()/"Overheads.csv" 

with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header
    categories = []
    values = []
    for row in reader:
            categories.append(row)
#create function
def overheads():
        fp = Path.cwd()/"summary_report.txt"
        with fp.open(mode = "w") as file:
            global categories, values
    #create empty list to append values inside
    #categories = []
    #values = [] 
    
    #with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        #reader = csv.reader(file)
        #next(reader) # skip header
        
        #for row in reader:
            #categories.append(row)
        
            for i in categories:
                values.append(float(i[1]))
            
            max_value = max(values)
        
        #index_of_max_value = [index for index, item in enumerate(values) if item == max_value][0]
        
<<<<<<< HEAD
            maxindex = 0
            for index, item in enumerate(values):
                list2 = []
                if item == max_value:
                    maxindex = index
            
            highest_overhead = categories[maxindex][0]
            #print(categories[index_of_max_value][0])
            highest_overhead_value = float(categories[maxindex][1])
            
            list2 = [f"Highest Overhead Category: {highest_overhead}, Amount: {highest_overhead_value}"]
            
            for i in list2:
                file.writelines(f"{i}\n")
#overheads()
#execute function 
=======
        for index, item in enumerate(values):
            if item == max_value:
                index_of_max_value = index

        highest_overhead = categories[index_of_max_value][0]
        highest_overhead_value = float(categories[index_of_max_value][1])
        
        return f"Highest Overhead Category: {highest_overhead}, Amount: {highest_overhead_value}"
        
print(overheads())
#executes function 
>>>>>>> 4daccad0562886af857108bf05b2968aa2863fd1


    

            

        
        




