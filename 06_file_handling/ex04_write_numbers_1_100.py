# create and open a file in write mode and name it numbers.txt
# use a loop to write a number and add a number in new line the range from 1 to 100
# print a confirmation message

with open("numbers.txt","w") as f:
    
    f.write("\n".join(str(i) for i in range(1,101)))
    
print("Numbers 1–100 saved successfully to numbers.txt ✅")