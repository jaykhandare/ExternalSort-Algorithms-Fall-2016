# creating data
import sys
import random
import time


def create_data(size):
        
    fo = open("data.csv", "w")
    for i in range(size):
        fo.write(str(random.randint(1,sys.maxsize-1)))
        fo.write(" \n ")

    fo.close()
