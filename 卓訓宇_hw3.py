#1-1
import csv
with open("train_feature.csv", "r") as hwfile:
    hwreader = csv.reader(hwfile)
    a = next(hwreader)
    print(a)
#1-2
import csv
with open("train_feature.csv", "r") as hwfile:
    hwreader = csv.reader(hwfile)
    A = [i for i in hwfile]
    print(A[-2:])
    


#2
try: 
    x = 1
    print( x * y )
except NameError: print('Undefined variable is what i want!')



#3
def haveseven(X):
    for i in range(1,X+1):
        if str(7) in str(i):
            print(i)
   
haveseven(30)


#4
import mod
mod.funconcat(mod.A, mod.B)


#5
import mod
mod.funprod(1,2,3,4,5,6)