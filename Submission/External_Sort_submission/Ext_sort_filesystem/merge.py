import sys
import time

def function(value,ptr):
    temp = int(ptr[value].readline())
    return (temp) 

def merger1(chunksize,rng,intr):

    txt = "intrim1_" + str(intr) + ".csv"
    f_out = open(txt,"w")
    ptr = []
    counter = [0]*5
    val = [0]*5
    for i in range(5):
        txt = "sorted_" + str(i+rng) + ".csv"
        f = open(txt,"r")
        ptr.append(f)    
    
    for i in range(5):
        val[i] = function(i,ptr)
    
    while True:    
        if(min(counter) == chunksize):
            break
    
        for i in range(5):
            if(val[i] <= min(val) and val[i] != sys.maxsize ):
                f_out.write(str(val[i]))
                f_out.write("\n")
                counter[i] = counter[i]+1
                if(counter[i] < chunksize):
                    val[i] = function(i,ptr)
                else:
                    val[i] = sys.maxsize

    for i in range(5):
        ptr[i].close()
   
    f_out.close()

def merger2(chunksize,rng,intr):

    txt = "intrim2_" + str(intr) + ".csv"
    f_out = open(txt,"w")
    ptr = []
    counter = [0]*2
    val = [0]*2
    for i in range(2):
        txt = "intrim1_" + str(rng+i) + ".csv"
        f = open(txt,"r")
        ptr.append(f)    
    
    for i in range(2):
        val[i] = function(i,ptr)
    
    while True:    
        if(min(counter) == chunksize):
            break
    
        for i in range(2):
            if(val[i] <= min(val) and val[i] != sys.maxsize ):
                f_out.write(str(val[i]))
                f_out.write("\n")
                counter[i] = counter[i]+1
                if(counter[i] < chunksize):
                    val[i] = function(i,ptr)
                else:
                    val[i] = sys.maxsize

    for i in range(2):
        ptr[i].close()
   
    f_out.close()

def merger3(chunksize):

    f_out = open("final_sorted_data.csv","w")
    ptr = []
    counter = [0]*2
    val = [0]*2
    for i in range(2):
        txt = "intrim2_" + str(i) + ".csv"
        f = open(txt,"r")
        ptr.append(f)    
    
    for i in range(2):
        val[i] = function(i,ptr)
    
    while True:    
        if(min(counter) == chunksize):
            break
    
        for i in range(2):
            if(val[i] <= min(val) and val[i] != sys.maxsize ):
                f_out.write(str(val[i]))
                f_out.write("\n")
                counter[i] = counter[i]+1
                if(counter[i] < chunksize):
                    val[i] = function(i,ptr)
                else:
                    val[i] = sys.maxsize

    for i in range(2):
        ptr[i].close()
   
    f_out.close()
