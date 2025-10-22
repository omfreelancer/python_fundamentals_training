# import re
# ask user for input
# use re.sub to replace all digits (0-9) to "*"
# print the same input but digits replaced with "*"

import re
user_input = input("Enter a string: ")
cleared_text = re.sub(r'[\d]','*',user_input)
print("Result:",cleared_text)