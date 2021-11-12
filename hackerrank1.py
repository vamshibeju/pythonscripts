#Task
#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of 2 to 5 , print Not Weird
#If  is even and in the inclusive range of 6 to 20 , print Weird
#If  is even and greater than 20, print Not Weird

n = int(input("please enter the number"))

if n % 2 != 0 or n in range(6,21):
   print('Weird')
elif n%2 == 0:
    print('Not Weird')
