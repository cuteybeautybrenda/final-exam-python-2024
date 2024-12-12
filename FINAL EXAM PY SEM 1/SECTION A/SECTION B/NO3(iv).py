def grade_students(mark):
    # Check if the mark is a valid number
    if not isinstance(mark, (int, float)):
        return 'Invalid Input'
    
    # Determine the grade based on the mark
    if mark >= 90:
        return 'A'
    elif 80 <= mark < 90:
        return 'B'
    elif 70 <= mark < 80:
        return 'C'
    elif 60 <= mark < 70:
        return 'D'
    else:
        return 'F'
    
# Testing the function with a valid mark
valid_mark = 85
print(grade_students(valid_mark))  # Expected Output: 'B'

# Testing the function with an invalid input
invalid_mark = 'eighty five'
print(grade_students(invalid_mark))  # Expected Output: 'Invalid Input'


