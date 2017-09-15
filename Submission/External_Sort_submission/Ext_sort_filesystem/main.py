# main file
import generate as start
import divide as div
import sort as s
import merge as m
import os
import time
import simple_sort as ss

size = 10000
no_parts = 20
part_size = int(size/no_parts)
res = open("result.txt","a")
res.write("Total number of integers in dataset = "+str(size)+"\n")

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

# clearing space
#------------------------------------------------------------------------------
for i in range(20):
    txt = "data_" + str(i) + ".csv"
    os.remove(txt)

#merging 5 sorted partitions at a time*4
#------------------------------------------------------------------------------
t1 = time.time()
m.merger1(part_size,0,0)
m.merger1(part_size,5,1)
m.merger1(part_size,10,2)
m.merger1(part_size,15,3)
t2 = time.time()
print("Time taken to perform first level of merging = ",t2-t1)
res.write("Time taken to perform first level of merging = "+ str(t2-t1)+"\n")

# clearing space
#------------------------------------------------------------------------------
for i in range(20):
    txt = "sorted_" + str(i) + ".csv"
    os.remove(txt)

#merging 2 intrim buffers at a time*2
#------------------------------------------------------------------------------
t1 = time.time()
m.merger2(part_size*5,0,0)
m.merger2(part_size*5,2,1)
t2 = time.time()
print("Time taken to perform second level of merging = ",t2-t1)
res.write("Time taken to perform second level of merging = "+str(t2-t1)+"\n")

# clearing space
#------------------------------------------------------------------------------
for i in range(4):
    txt = "intrim1_" + str(i) + ".csv"
    os.remove(txt)

#final merge of 2 intrim2 buffers
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

# clearing space
#------------------------------------------------------------------------------
for i in range(2):
    txt = "intrim2_" + str(i) + ".csv"
    os.remove(txt)

os.remove("final_sorted_data.csv")

#calling simple sort for generated data
#------------------------------------------------------------------------------
t = ss.simplesort(size)
print("Total time taken to perform simple merge sort = ",t)
res.write("Total time taken to perform simple merge sort = "+str(t)+"\n")
res.write("\n")
res.close()

# clearing space
#------------------------------------------------------------------------------
os.remove("simple_sorted.csv")
os.remove("data.csv")
