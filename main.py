# main.py

# Функция для нахождения максимального значения
def find_max(numbers):
    if not numbers:  # Проверка, что список не пустой
        return None  # Возвращаем None, если список пустой
    
    max_value = numbers[0]
    for num in numbers[1:]:  # Начинаем с второго элемента списка
        if num > max_value:
            max_value = num
    return max_value

# Пример использования функции
if __name__ == "__main__":
    # Тестовые данные
    numbers1 = [3, 5, 7, 2, 8]
    numbers2 = [10, 20, 5, 15, 25, 30]
    numbers3 = [-5, -1, -10, -3]
    numbers4 = []

    # Печать результатов
    print("Максимальное значение в numbers1:", find_max(numbers1))  # Ожидаемый результат: 8
    print("Максимальное значение в numbers2:", find_max(numbers2))  # Ожидаемый результат: 30
    print("Максимальное значение в numbers3:", find_max(numbers3))  # Ожидаемый результат: -1
    print("Максимальное значение в numbers4:", find_max(numbers4))  # Ожидаемый результат: None
