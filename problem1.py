def student_info():
    print("Name: Abdul Samad Riaz")
    print("Student ID: BSE-25S-630")
    print("Profession: Software Engineering")

student_info()


def greater_than(numbers,value):
    result = []
    for num in numbers:
        if num > value:
            result += [num]
    return result
numbers = [10, 25, 5, 40, 15, 60, 8]
value = 20
answer = greater_than(numbers,value)
print(answer)

            