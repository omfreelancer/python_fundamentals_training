#the function fibonacci(n):
    #if n == 1 return [0]
    #if n == 2 return [0,1]
    #else:
        # loop until len(list) = n
        #Compute next_num = last two elements sum.
        #append to the list
    #return the list
#the main progrma:
    #ask the user a number
    #chech if it is a number if not reask
    #check if n>=1 if not reask and print n must be greater than 0.
    #apply the function
    #print the function

def fibonacci(n):

    if n == 1:
        return [0]
    
    elif n ==2:
        return [0,1]
    
    else:
        numbers = [0,1]

        while len(numbers) < n:
            last_number = numbers[-1] + numbers[-2]
            numbers.append(last_number)

        return numbers

while True:
    user_input = input("Enter a number: ")

    if not user_input.isdigit():
        print("Invalid input. Enter a number.")
        continue
    
    else:
        number = int(user_input)

        if number <= 0:
            print("Number must be greater than 0.")
            continue

        sequence = fibonacci(number)

        print("Fibonacci sequence:",", ".join(map(str,sequence)))
        break