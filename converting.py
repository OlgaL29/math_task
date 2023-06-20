import math
import sys
# Лазарева Ольга Андреевна  , варинант 9, группа 44-22-114
def convert_value(*args):
    results = []
    for x in args:
        try:
            if x <= 2:
                y = 6.811 * (1 + math.exp(6.81 * x))
            else:
                y = math.sqrt(x) + math.exp(-x)
            results.append(y)
        except ValueError:
            results.append(None)
    return results

# Get command line input
inputs = sys.argv[1:]
if not inputs:
    print("No input values provided.")
else:
    try:
        values = [float(x) for x in inputs]
        results = convert_value(*values)
        for x, y in zip(values, results):
            if y is not None:
                print(f"For x = {x}, y = {y}")
            else:
                print(f"Invalid input for x = {x}.")
    except ValueError:
        print("Invalid input. Please provide numeric values.")