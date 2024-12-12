# Taking input for student's details
student_name = input("Enter student name: ")
student_number = input("Enter student number: ")
programming_marks = float(input("Enter marks for Programming: "))
data_science_marks = float(input("Enter marks for Data Science: "))
computer_applications_marks = float(input("Enter marks for Computer Applications: "))

# Calculating the average mark
average_mark = (programming_marks + data_science_marks + computer_applications_marks) / 3

# Displaying the student details along with the average mark
print("\n--- Student Details ---")
print(f"Student Name: {student_name}")
print(f"Student Number: {student_number}")
print(f"Programming Marks: {programming_marks}")
print(f"Data Science Marks: {data_science_marks}")
print(f"Computer Applications Marks: {computer_applications_marks}")
print(f"Average Mark: {average_mark:.3f}")
