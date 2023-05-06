#Задача 32: Определить индексы элементов массива (списка), 
#значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

def task_30():
  first_Number = int(input("Enter the first number of the list, please: "))
  difference_Number = int(input("Enter the difference between the elements, please: "))
  size_List = int(input("Enter the size of the list, please: "))
  use_List = [(first_Number + i*difference_Number) for i in range(size_List)]
  print (*use_List)