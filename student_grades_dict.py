student_grades = {
            "Student1" : 'A',
            "Student2" : 'F',
            "Student3" : 'C',
            "Student4" : 'D',
            "Student5" : 'B',
}

#Printing the entire dictionary
print(student_grades)

#Accessing the grade of the 3rd student
print("Grade of third student is: ", student_grades["Student3"])

#Updating the grade of the 2nd student
student_grades["Student2"] = 'A'
print(student_grades)

#Deleting the entry of 5th student
del student_grades["Student5"]
print(student_grades)

#Printing the last key value pairs
last_key = list(student_grades.keys())[-1]
last_value = student_grades[last_key]
print("The last key-value is", last_key, ":", last_value)

