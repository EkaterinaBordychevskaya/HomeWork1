try:
    x=int(input("Введите делимое число: "))
    y=int(input("Введите делитель: "))
    result=x/y
except ZeroDivisionError:
    print("Ошибка! Нельзя делить на ноль.")
else:
    print(f"Результат деления {x} на {y} равен {result}")
