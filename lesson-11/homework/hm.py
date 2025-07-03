def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a/b
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius
# geometry/__init__.py
from .circle import calculate_area, calculate_circumference
def read_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"Error: {e}"
    
    ef write_file(filepath, content):
    try:
        with open(filepath, 'w') as file:
            file.write(content)
            return "Write successful."
    except Exception as e:
        return f"Error: {e}"
from geometry import calculate_area, calculate_circumference
from file_operations import write_file, read_file

radius = 7
area = calculate_area(radius)
circumference = calculate_circumference(radius)

text = f"Radius: {radius}\nArea: {area:.2f}\nCircumference: {circumference:.2f}"
write_file("circle_info.txt", text)

print("File contents:")
print(read_file("circle_info.txt"))
