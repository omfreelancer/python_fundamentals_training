def average(numbers):
    assert isinstance(numbers,list), "Input should be a list."
    assert numbers, "List cannot be empty"
    assert all(isinstance(number,(int,float)) for number in numbers), \
          "All items must be numbers"

    return sum(numbers) / len(numbers)