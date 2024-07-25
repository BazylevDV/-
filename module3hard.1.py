data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]# Объединение всех элементов в одну структуру данных

def calculate_structure_sum(data):# Инициализация общей суммы
    total_sum = 0

    def process_element(element):
        nonlocal total_sum# Использование nonlocal для изменения переменной total_sum из внешней функции
        if isinstance(element, int):# Если элемент - целое число, добавляем его к общей сумме
            total_sum += element
        elif isinstance(element, str):# Если элемент - строка, добавляем её длину к общей сумме
            total_sum += len(element)
        elif isinstance(element, (list, tuple, set)):# Если элемент - словарь, рекурсивно обрабатываем каждый ключ и значение
            for item in element:
                process_element(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                process_element(key)
                process_element(value)

    process_element(data)# Запуск рекурсивной обработки для всей структуры данных
    return total_sum# Возвращение общей суммы
result = calculate_structure_sum(data_structure)# Вызов функции для подсчёта суммы всех чисел и длин всех строк
print(result)
