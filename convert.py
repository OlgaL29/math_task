import math
import sys
# Лазарева Ольга Андреевна  , варинант 9, группа 44-22-114
def convert_value(x):
    if x <= 2:
        y = 6.811 * (1 + math.exp(6.81 * x))
    else:
        y = math.sqrt(x + math.exp(-x)) 
    return y

try:
    x = float(input("Введите числовое значение: "))
    result = convert_value(x)
    print("Результат:", result)
except ValueError:
    print("Неверный Ввод. Введите числовое значение.")