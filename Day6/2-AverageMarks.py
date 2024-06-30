marks_list = []
for i in range (5):
    marks =  int(input(f"enter marks for subject {i+1} :- "))
    marks_list.append(marks)

average = sum(marks_list) / len(marks_list)

if average >= 90:
    print("Grade A")
elif average >= 80:
    print("grade = B")
elif average >= 70:
    print("grade = C")
elif average >= 60:
    print("grade = D")
else:
        print("grade = F")