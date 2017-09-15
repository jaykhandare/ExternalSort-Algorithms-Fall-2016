#mainfile_database

import time as t
import connection as c
import populate as p
import divide as d
import sorting as s
import merging as m

size = 100
no_parts = 20
part_size = int(size/no_parts)

cur,conn = c.connect()

t1 = t.time()
p.create(cur,conn,size)
t2 = t.time()

print("Time taken to create a database of ",size,"entries = ",t2-t1)

t0 = t.time() #external_sort starts here

t1 = t.time()
d.partition(cur,conn,no_parts,part_size)
t2 = t.time()
print("Time taken to divide database into ",no_parts,"partisions = ",t2-t1)


t1 = t.time()
s.sorter(cur,conn,no_parts,part_size)
t2 = t.time()
print("Time taken to sort all partitions = ",t2-t1)


t1 = t.time()
# merging 5 tables at a time
m.merge1(cur,conn,5,part_size,0,0)
m.merge1(cur,conn,5,part_size,5,1)
m.merge1(cur,conn,5,part_size,10,2)
m.merge1(cur,conn,5,part_size,15,3)

# merging 2 intrim tables at a time
m.merge2(cur,conn,2,part_size*5,0,0)
m.merge2(cur,conn,2,part_size*5,2,1)

# final merge
m.merge3(cur,conn,2,part_size*5*2)

t2 = t.time()

print("Time taken to merge all partitions = ",t2-t1)

t3 = t.time()

print("Time taken to perform external sort on a database with ",size,"entries = ",t3-t0)

conn.commit()