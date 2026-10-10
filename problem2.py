def remove_duplicates(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result += [num]
    return result
numbers = [23,34,45,23,45,80,90,80]
answer = remove_duplicates(numbers)
print(answer)