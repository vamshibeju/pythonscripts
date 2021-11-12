#Example
#The provided code stub reads and integer,n , from STDIN. For all non-negative integers i <n  , print  i2
#The list of non-negative integers that are less than n=3 is [0,1,2]. Print the square of each number on a separate line.
#op - 0,1,4
n = int(input("enter the number"))
if n > 1:
    for i in range(n):
        print(i*i)