#The provided code stub reads two integers,  and , from STDIN.

#Add logic to print two lines. The first line should contain the result of integer division,  // . 
#The second line should contain the result of float division,  / .

#No rounding or formatting is necessary.

a= int(input("enter the number"))
b = int(input("enter the number"))
division= a//b #floor division
print(division)
floatdivision= a/b
print(float(floatdivision))