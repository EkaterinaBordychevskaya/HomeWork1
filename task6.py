x=int(input("Введите число: "))

try:
  import math
  res=math.sqrt(num)
except ValueError:
  print("Вы ввели отрицательное число")
except ImportError:
  print("Ошибка подключения math")
else:
  print(res)
