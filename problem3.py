def count_occurrences(numbers, target):
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    return  count
numbers = [10, 20, 10, 30, 10, 40, 20]
target = 10
answer = count_occurrences(numbers,target)
print(answer)