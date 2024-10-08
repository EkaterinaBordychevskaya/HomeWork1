x=input("Введите число: ")

try:
  x=float(x)
except ValueError as e:
  print ("Вы ввыели неверную строку")
  print (e)
else: print (x)
