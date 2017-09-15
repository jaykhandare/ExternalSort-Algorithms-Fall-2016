# creating partitions  
import time

def divide(size,no_parts):
    
    f_in = open("data.csv", "r")    

    for i in range(no_parts):
        txt = "data_" + str(i) + ".csv"
        f = open(txt,"w")
        cnt = 0
            
        while True:
            line = f_in.readline()
            f.write(line)
            cnt = cnt+1
            if (cnt == size):
                break
        f.close()

    f_in.close()
