try:
    x=int(input("Введите делимое число"))
    y=int(input("Введите делитель"))
    result=x/y
except ZeroDivisionError:
    print("Ошибка! Нельзя делить на ноль.")
except TypeError:
    print("Ошибка! Введено значение неподходящего типа.")
else:
    print("Результат деления {x} на {y} равен {result}")
