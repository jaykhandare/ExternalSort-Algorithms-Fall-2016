# main file
import creating_data as start
import divide as div
import sorting as s
import merging as m
import os
import time
import simple_sort as ss

size = 1000000000
no_parts = 20
part_size = int(size/no_parts)
print("Begin\n")
res = open("result.txt","a")
res.write("\nTotal number of integers in dataset = "+str(size)+"\n")

#creating data
#------------------------------------------------------------------------------
t1 = time.time()
start.create_data(size)
t2 = time.time()
print("Dataset with ",size,"entries created.\n")
print("Time taken to create dataset = ",t2-t1)
res.write("Time taken to create dataset = "+str(t2-t1)+"\n")

#starting external_sort
#------------------------------------------------------------------------------
ti = time.time()
#making partitions
#------------------------------------------------------------------------------
t1 = time.time()
div.divide(part_size,no_parts)
t2 = time.time()
print("Time taken to divide and store dataset = ",t2-t1)
res.write("Time taken to divide and store dataset = "+str(t2-t1)+"\n")

#sorting partitions
#------------------------------------------------------------------------------
t1 = time.time()
s.sorter(part_size,no_parts)
t2 = time.time()
print("Time taken to sort all partitions and store them = ",t2-t1)
res.write("Time taken to sort all partitions and store them = "+ str(t2-t1)+"\n")

#merging 5 chunks at a time
#------------------------------------------------------------------------------
t1 = time.time()
m.merger1(part_size,0,0)
m.merger1(part_size,5,1)
m.merger1(part_size,10,2)
m.merger1(part_size,15,3)
t2 = time.time()
print("Time taken to perform first level of merging = ",t2-t1)
res.write("Time taken to perform first level of merging = "+ str(t2-t1)+"\n")

#merging 2 intrim chunks at a time
#------------------------------------------------------------------------------
t1 = time.time()
m.merger2(part_size*5,0,0)
m.merger2(part_size*5,2,1)
t2 = time.time()
print("Time taken to perform second level of merging = ",t2-t1)
res.write("Time taken to perform second level of merging = "+str(t2-t1)+"\n")

#final merge of 2 intrim2 chunks
#------------------------------------------------------------------------------
t1 = time.time()
m.merger3(part_size*5*2)
t2 = time.time()
print("Time taken to perform last level of merging = ",t2-t1)
res.write("Time taken to perform last level of merging = "+str(t2-t1)+"\n")

# concluding external sort
#------------------------------------------------------------------------------
tf = time.time()
print("Total time taken for complete external sort = ",tf-ti)
res.write("Total time taken for complete external sort = "+str(tf-ti)+"\n")

#calling simple sort for generated data
#------------------------------------------------------------------------------
t = ss.simplesort(size)
print("Total time taken to perform simple merge sort = ",t)
res.write("Total time taken to perform simple merge sort = "+str(t)+"\n")
res.write("Simple Merge sort cannot be performed on this dataset."+"\n")
res.write("\n")

res.close()

#deleting the buffers
#------------------------------------------------------------------------------
#os.remove("data.csv")
#os.remove("final_sorted_data.csv")
#os.remove("simple_sorted.csv")

for i in range(20):
    txt = "data_" + str(i) + ".csv"
    os.remove(txt)
    txt = "sorted_" + str(i) + ".csv"
    os.remove(txt)

for i in range(4):
    txt = "intrim1_" + str(i) + ".csv"
    os.remove(txt)

for i in range(2):
    txt = "intrim2_" + str(i) + ".csv"
    os.remove(txt)