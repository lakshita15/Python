f = open("F1.txt",'r')
student_no = 0

while True:
    student_no = student_no+1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f" The marks of student { student_no} in English are {m1}")
    print(f" The marks of student { student_no} in hindo are {m2}")
    print(f" The marks of student { student_no} in maths are {m3}")

    print(line)