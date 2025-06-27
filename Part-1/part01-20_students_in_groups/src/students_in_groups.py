student_number = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))

if student_number % group_size == 0:
    print(f"Number of groups formed: {student_number / group_size}")
else:
    print(f"Number of groups formed: {student_number / group_size + 1}")