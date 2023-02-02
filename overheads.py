from pathlib import Path  
import csv    #import file 

# create file path to csv report
file_path= Path.cwd()/"csv_reports"/"Overheads.csv" 

with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create empty lists to store overhead transactions
    categories = []
    values = []

    for row in reader:
            # append overhead transactions to empty list
            categories.append(row)
#create function
def overheads():
    """
    function calculates the highest overhead category and correponding percentage
    function writes the highest overhead details to a summary report .txt file
    """

    # create file path to summary_report.txt
    fp = Path.cwd()/"summary_report.txt"
    with fp.open(mode = "w") as file:
            global categories, values

            # store overhead values in empty list
            for i in categories:
                values.append(float(i[1]))
            
            # identify highest overhead value
            max_value = max(values)

            # initialise variable
            maxindex = 0
            # for loop to find the max value within the list
            # enumerate as a counter to run through the index within list
            for index, item in enumerate(values):
                    # list to store the f string for highest overhead category and value
                    list2 = []
                    if item == max_value:
                        maxindex = index

            # variable to store the highest overhead category    
            highest_overhead = categories[maxindex][0]
            # variable to store the highest overhead value
            highest_overhead_value = float(categories[maxindex][1])

            # list to store the highest overhead category and value    
            list2 = [f"[HIGHEST OVERHEADS] {highest_overhead.upper()}: {highest_overhead_value}%"]
            
            # write highest overhead and value to summary_report.txt
            for i in list2:
                file.writelines(f"{i}\n")




    
1
1          
1
 1       
  1      
1v

1
a
dasdadasdasss
sets
set
sets
sets
sets
sets
sets
sets
anda
andc
zip
zipz
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x

x
x
x
x
x

x
x
x
x
x
x
x
x
x

x
x
x

x

x
x
x

xx
x

x

x
x
x

x
x
xx

x
x

x
xx

x
x
x

x
x
xx

x
x

x
xx

x
x
x

x
x
xx

x
x

x
xx

x
x
x

x
x
xx

x
x

x
xx

x
x
x

x
x
xx

x
x

x
xx

x
x
x

x
x
xx

x
x

x
xx

x
x
x

x
x
xx

x
x

x
xx

x
x
x

x
x
xx

x
x