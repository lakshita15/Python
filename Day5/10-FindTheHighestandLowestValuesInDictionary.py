student_marks = {
    "s1": 34,
    "s2": 45,
    "s3": 67,
    "s4": 55,
    "s5": 89,
    "s6": 67,
}

# Initialize highest to a very low number
highest = -float("inf")
lowest = float("inf")
for name in student_marks:
    value = student_marks[name]

    if value > highest:
        highest = value

    if value < lowest:
        lowest = value

print(highest , lowest)
