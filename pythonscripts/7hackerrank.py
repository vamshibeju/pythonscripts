#delimeter split with space and join with "-"
value = str(input("enter the string"))
newvalue= value.split(" ")
joinvalue= "-".join(newvalue)
print(joinvalue)