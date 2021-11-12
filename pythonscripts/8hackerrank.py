#We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
#Let's try to understand this with an example.
#You are given an immutable string, and you want to make changes to it
#>>> string = "abracadabra"
#You can access an index by:
#>>> print string[5]
#a
def mutate_string(string, position, character):
    value = list(string)
    value[position]=character
    newvalue="".join(value)
    return newvalue
if __name__ == '__main__':

    mutate_string("luck",0,"f")