def second_largest(numbers):
    largest = float('-inf')
    second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num

        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        return None

    return second


numbers = [12, 45, 23, 67, 34, 67, 56]

answer = second_largest(numbers)
print(answer)