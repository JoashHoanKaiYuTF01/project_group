from pathlib import Path  
import csv    #import file 

#create function
def overheads():
    global categories, values
    #create empty list to append values inside
    categories = []
    values = []
    current_dir = Path.cwd()/"Overheads.csv" 
    
    with current_dir.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header
        
        for row in reader:
            categories.append(row)
        
        for i in categories:
            values.append(float(i[1]))
        
        max_value = max(values)
        index_of_max_value = [index for index, item in enumerate(values) if item == max_value][0]
        
        highest_overhead = categories[index_of_max_value][0]
        highest_overhead_value = float(categories[index_of_max_value][1])
        
        return f"Highest Overhead Category: {highest_overhead}, Amount: {highest_overhead_value}"
        
print(overheads())
#execute function x




