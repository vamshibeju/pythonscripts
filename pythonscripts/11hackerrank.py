#Regularexpression
"""For example:
Your task is to provide two regular expressions regex_integer_in_range and regex_alternating_repetitive_digit_pair. Where:

regex_integer_in_range should match only integers range from 100000 to 999999  inclusive

regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.

121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits."""

import re
#value = int(input("enter a number"))
#if value in range(100000,999999):
 #   print("value is correct")
#else:
regex_integer_in_range = r'^[1-9][\d]{5}$'	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)',# Do not delete 'r'.



P =(input("enter the number"))

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)