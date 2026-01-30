# Problem 9: Find average of numbers in a list
# Find and fix the error

numbers = [10, 20, 30, 40, 50]

if numbers:  # check that the list is not empty
    total = sum(numbers)
    average = total / len(numbers)
    print(f"Average: {average}")
else:
    print("Error: The list is empty, cannot compute average.")
