def grade_students(mark):
    # Check if the mark is a valid number
    if not isinstance(mark, (int, float)):
        return 'Invalid Input'
    
    # Determine the grade and message based on the mark
    if mark >= 90:
        return 'A', 'Excellent'
    elif 80 <= mark < 90:
        return 'B', 'Excellent'
    elif 70 <= mark < 80:
        return 'C', 'Good'
    elif 60 <= mark < 70:
        return 'D', 'Satisfactory'
    else:
        return 'F', 'Needs Improvement'

# Testing the function with a valid mark
valid_mark = 85
grade, message = grade_students(valid_mark)
print(f"The grade for the mark {valid_mark} is: {grade}, Message: {message}")

# Testing the function with an invalid input
invalid_mark = 'eighty five'
print(grade_students(invalid_mark))  # Expected Output: 'Invalid Input'

