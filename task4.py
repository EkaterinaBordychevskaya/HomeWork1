list=[3, 7, 11, 2, 0]

i=int(input("Введите индекс элемента: "))

try:
  print (list[i-1])
except IndexError as e:
  print("В списке нет элемента с таким индексом")
  print(e)
