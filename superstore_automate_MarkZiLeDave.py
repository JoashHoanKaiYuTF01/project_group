from pathlib import Path
import matplotlib.pyplot as plt # ensure you have intalled matplotlib before importing it. available in the project brief.
import csv

#--------------- PART 1: This part of the program is completed for you --------------#

# create a file to csv file.
fp = Path.cwd()/"superstore_transaction.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create 3 empty lists to store profit and quantity by each cluster
    cluster1 = [] 
    cluster2 = []
    cluster3 = []

    # append profit and quantity as a list back to each empty list
    for row in reader:
                
        if row[4] == "Cluster 1":
            cluster1.append([row[13], row[14]])
        elif row[4] == "Cluster 2":
            cluster2.append([row[13], row[14]])
        else:
            cluster3.append([row[13], row[14]])

#---------------------------- PART 2: Insert your own code ---------------------------#
# 1. Calculate the total profit and total quantity using cluster 1,2,3 variables from part 1
# 2. Write the calculated profit to a txt file. Name it as cluster_report.txt.


# creates an empty list to store total cluster profit
# cluster_profit = [total_profit(cluster1),total_profit(cluster2),total_profit(cluster3)]
cluster_profit = [0, 0, 0]
# creates an empty list to store total cluster quantity
# cluster_quantity = [total_quantity(cluster1),total_quantity(cluster2),total_quantity(cluster3)]
cluster_quantity = [0, 0, 0]

# for loop with enumerate() returns the sequence number and letter pair
for cluster_no, cluster in enumerate([cluster1, cluster2, cluster3]):
    for i in cluster:
        # .replace to remove the "$" and "," in order to make the value a float
        # [0] indicates the first position of the list
        # sums the profit and quantity and profit
        # automatically moves the sums of the quantity and profit into cluster_profit and cluster_quantity
        cluster_profit[cluster_no] += float(i[0].replace("$","").replace(",",""))
        cluster_quantity[cluster_no] += float(i[1])

# creates a new list which consistws of profit and quantity obtained using the for loop
# uses \n to form a new line for each cluster
txt_file = ["PROFIT REPORT",
            "\n=============",
            f"\nCluster 1: ${cluster_profit[0]}",
            f"\nCluster 2: ${cluster_profit[1]}",
            f"\nCluster 3: ${cluster_profit[2]}",
            "\n\nQUANTITY REPORT",
            "\n===============",
            f"\nCluster 1: {cluster_quantity[0]}",
            f"\nCluster 2: {cluster_quantity[1]}",
            f"\nCluster 3: {cluster_quantity[2]}"]

# creates a path object for "cluster_report.txt"
file_path = Path.cwd()/"cluster_report.txt"
# use mode = "w" to write code into a .txt file
with file_path.open(mode = "w", encoding= "UTF-8") as file:
    # use .writelines since txt_file is a list
    file.writelines(txt_file)



#--------------- PART 3: This part of the program is completed for you  --------------#

# This part of the program plots the profits and quantities by clusters.
# The values profits and quantities are hard-coded, so it is not link to part 2. 
# Even if part 2 does not work, part 3 can still be executed.
# Simply execute the code and the plot will be saved as an image file.
# Click on the png file in the explorer panel to see the barplot.

# Do not worry about how the code below works.
# It is an example of visualising data using Python. 
# You will learn about data visulisation in analytics module in year 2. 

cluster_profit = [133426, 43684, 109224] # hardcoded profit by clusters 
cluster_quantity = [18632, 8716, 10524] # hardcoded quantity sold by clusters. 
fig, axs = plt.subplots(2, figsize = (10,7))
fig.suptitle("SuperStore Business Performance")
cluster = ["cluster 1", "cluster 2", "cluster 3"]
axs[0].bar(cluster, cluster_profit)
axs[1].bar(cluster, cluster_quantity)
axs[0].set_xlabel("Profit by Clusters")
axs[1].set_xlabel("Quantity Sold by Clusters")
axs[0].set_ylabel("Profit ($)")
axs[1].set_ylabel("Quantity (000s)")
fig.savefig("cluster_barplot.png") 
plt.imread("cluster_barplot.png")
plt.show()












