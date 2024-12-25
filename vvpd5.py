import math
 
def maclaurin_cos(x, iterations=10):
    """
    Вычисляет косинус с использованием ряда Маклорена.

    Формула:
    cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + ...

    Параметры:
        x (float): значение x, для которого вычисляется косинус
        iterations (int): количество итераций ряда

    Возвращает:
        float: приближённое значение cos(x)
    """
    result = 0
    for n in range(iterations):
        term = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
        result += term
    return result

def maclaurin_exp_minus_one(x, iterations=10):
    """
    Вычисляет e^x - 1 с использованием ряда Маклорена.

    Формула:
    e^x - 1 = x + x^2/2! + x^3/3! + ...

    Параметры:
        x (float): значение x, для которого вычисляется e^x - 1
        iterations (int): количество итераций ряда

    Возвращает:
        float: приближённое значение e^x - 1
    """
    if x <= -1 or x >= 1:
        raise ValueError("x должен быть в пределах (-1, 1) для данной формулы.")

    result = 0
    for n in range(1, iterations + 1):
        term = (x ** n) / math.factorial(n)
        result += term
    return result

def maclaurin_sqrt_one_minus_x(x, iterations=10):
    """
    Вычисляет sqrt(1 - x) с использованием ряда Маклорена.

    Формула:
    sqrt(1 - x) = 1 - x/2 - (x^2)/(8) - (x^3)/(16) + ...

    Параметры:
        x (float): значение x, для которого вычисляется sqrt(1 - x)
        iterations (int): количество итераций ряда

    Возвращает:
        float: приближённое значение sqrt(1 - x)
    """
    if x <= -1 or x > 1:
        raise ValueError("x должен быть в пределах (-1, 1] для данной формулы.")

    result = 0
    for m in range(iterations):
        term = ((-1)**m) * (math.prod(range(1, 2 * m, 2)) / (2 * m * math.factorial(m))) * (x ** m)
        result += term
    return result

def user_menu():
    """
    Реализует пользовательское меню для выбора формулы и ввода значения x.
    """
    while True:
        print("\nМеню:")
        print("1. Вычислить cos(x) с использованием ряда Маклорена")
        print("2. Вычислить e^x - 1 с использованием ряда Маклорена")
        print("3. Вычислить sqrt(1 - x) с использованием ряда Маклорена")
        print("4. Выход")

        choice = input("Выберите опцию (1/2/3/4): ")

        if choice == '1':
            try:
                x = float(input("Введите значение x: "))
                result = maclaurin_cos(x)
                print(f"Приближённое значение cos({x}) = {result}")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '2':
            try:
                x = float(input("Введите значение x (должно быть в пределах (-1, 1)): "))
                result = maclaurin_exp_minus_one(x)
                print(f"Приближённое значение e^{x} - 1 = {result}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == '3':
            try:
                x = float(input("Введите значение x (должно быть в пределах (-1, 1]): "))
                result = maclaurin_sqrt_one_minus_x(x)
                print(f"Приближённое значение sqrt(1 - {x}) = {result}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    user_menu()

