# List of integers
numbers = [4, 7, 2, 9, 12, 15]

# Initialize a variable to store the sum of odd numbers
sum_of_odds = 0

# Iterate through the list
for num in numbers:
    # Check if the number is odd
    if num % 2 != 0:
        sum_of_odds += num  # Add the odd number to the sum

# Print the result
print("Sum of all odd numbers:", sum_of_odds)
