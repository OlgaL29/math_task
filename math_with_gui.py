import math
import tkinter as tk
from tkinter import messagebox
# Лазарева Ольга Андреевна  , варинант 9, группа 44-22-114-
def convert_value():
    try:
        x = float(entry.get())
        if x <= 2:
            y = 6.811 * (1 + math.exp(6.81 * x))
        else:
            y = math.sqrt(x + math.exp(-x))
        result_label.config(text=f"Результат: {y}")
    except ValueError:
        messagebox.showerror("Ошибка", "Неверный ввод. Введите числовое значение.")

window = tk.Tk()
window.title("Конвертер значений")
window.geometry("300x150")

input_label = tk.Label(window, text="Введите числовое значение:")
input_label.pack()
entry = tk.Entry(window)
entry.pack()

convert_button = tk.Button(window, text="Конвертировать", command=convert_value)
convert_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()