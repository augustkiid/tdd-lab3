def find_max(numbers):
    if not numbers:
        raise ValueError("Список пуст")

    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum
git add find_max.py
git commit -m "Добавлена функция find_max с проверкой на пустой список"

