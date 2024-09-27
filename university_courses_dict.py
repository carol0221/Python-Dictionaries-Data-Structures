universities_courses = {   
    "Harvard University": "Law",
    "Stanford University": "Computer Science",
    "Ateneo de Manila University" : "BS Management Engineering",
    "Oxford University": "Philosophy",
    "University of Santo Tomas" : "BS Nursing",
    "Princeton University": "Economics",
    "Yale University": "Political Science",
    "University of Chicago": "Sociology"
}

print(universities_courses)

print("The course of the third university is:", universities_courses["Ateneo de Manila University"])

universities_courses["University of Santo Tomas"] = "BS Accountancy"
print(universities_courses)

del universities_courses["Yale University"]
print(universities_courses)

last_key = list(universities_courses.keys())[-1]
last_value = universities_courses[last_key]
print("The last key-value pair is", last_key, ":", last_value)

