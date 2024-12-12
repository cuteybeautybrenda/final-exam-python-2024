def calculate_operations(num1, num2):
    # Sum
    sum_result = num1 + num2
    
    # Difference
    difference_result = num1 - num2
    
    # Product
    product_result = num1 * num2
    
    # Quotient (check to avoid division by zero)
    if num2 != 0:
        quotient_result = num1 / num2
    else:
        quotient_result = "Undefined (division by zero)"
    
    return sum_result, difference_result, product_result, quotient_result

# Example usage
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result, difference_result, product_result, quotient_result = calculate_operations(num1, num2)

print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")
