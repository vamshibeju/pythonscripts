#findout whether its a leapyear or not and use functions 
#if it is divisible by 4 and 400 then its a leap year 
#if it is divisible by 100 then its not a leap year 
def is_leap(year):
    leap= False    
    if year % 4 ==0 and  year % 100 == 0:
         if year % 400 == 0 :
            leap = True
            return leap
         else:
            leap = False
            return leap
    elif year % 4 ==0 and year % 100 !=0:
        leap= True
        return leap
    #elif year % 4 !=0 and year % 100 !=0 and year % 400 != 0:
    else:
        return leap
year= int(input("enter the year"))
print(is_leap(year))