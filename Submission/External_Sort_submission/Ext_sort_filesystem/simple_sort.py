# basic plain sort
import time
import var_sorts as s

def simplesort(size):

    k = 0
    arr = [1]*size
    t1 = time.time()

    for line in open("data.csv","r"):
        if line.strip():
            n = int(line)
            arr[k] = n
            k = k + 1

    arr = s.merge_sort(arr)

    f = open("simple_sorted.csv","w")
    for k in range(size):
        f.write(str(arr[k]))
        f.write("\n")

    t2 = time.time()

    return(t2-t1)    