def find_max(numbers):
    max_value = numbers[0]
    if numbers[1] > max_value:
        max_value = numbers[1]
    if len(numbers) > 2 and numbers[2] > max_value:
        max_value = numbers[2]
    return max_value
