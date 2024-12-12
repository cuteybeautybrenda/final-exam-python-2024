def grade_students(mark):
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
    