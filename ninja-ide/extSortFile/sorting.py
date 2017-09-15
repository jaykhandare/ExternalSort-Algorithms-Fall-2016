# sorting a partition with merge sort

import sorts as s

def sorter(chunksize,size):
        
    arr = [1]*chunksize

    for k in range(size):
        cnt = 0
        in_txt = "data_" + str(k) + ".csv"
        for line in open(in_txt,"r"):
            if line.strip():           
                n = int(line)
                arr[cnt] = n
                cnt = cnt+1

        out_txt = "sorted_" + str(k) + ".csv"
        f_out = open(out_txt,"w")
        arr = s.merge_sort(arr)
        for i in range(cnt):
            f_out.write(str(arr[i]))
            f_out.write("\n")
        
        f_out.close()
