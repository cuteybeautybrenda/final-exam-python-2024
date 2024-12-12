# Asking the user for the number of miles driven and gallons used
miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the number of gallons of gas used: "))

# Calculating miles per gallon (MPG)
mpg = miles_driven / gallons_used

# Displaying the result
print(f"The car's miles per gallon (MPG) is: {mpg:.2f}")
