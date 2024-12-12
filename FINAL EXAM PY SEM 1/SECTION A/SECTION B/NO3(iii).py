 # Define the grade_students function
def grade_students(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

# Test the function with a mark of 85
mark = 85
grade = grade_students(mark)
print(f"The grade for the mark {mark} is: {grade}")
