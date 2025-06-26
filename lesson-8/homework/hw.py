try:
    5/0
except ZeroDivisionError:
    print("You can't divide a number by zero!")
try:
    a= int(input('Enter Integer only:'))
    print(f'You entered the integer:{a}')
except ValueError:
    print("Error: That is not Valid Integer")

try:
    with open('test.py') as f:
        data = f.read()
except FileNotFoundError:
    print("File does not exist")

try:
    number1 = input('Enter Integer only: ')
    number2 = input('Enter Integer only: ')
    
    try:
        number1 = int(number1)
        number2 = int(number2)
    except ValueError:
        raise TypeError("Inputs must be integers.")

    print(f'You entered number: {number1}')
    print(f'You entered number: {number2}')
except TypeError as e:
    print(f"Error: {e}")
try:
    with open('example.txt','r') as file:
        content = file.read()
        print("file content:")
        print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error:You dont have Permission to access file")


try:
    l= [1,2,3,4,5,6]
    print(l[7])
except IndexError:
    print("Error : Index is out of range")

try:
    number = input("Enter a number: ")
    print(f"You entered: {number}")
except KeyboardInterrupt:
    print("Error: Input canceled by user.")
try:
    num1 = int(input("Enter number :"))
    num2 = int(input("Enter number :"))
    result = num1/num2
    print(f"Rusult: {result}")
except ArithmeticError:
    print("Accured an ArithmeticError")




try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except UnicodeDecodeError:
    print("Error: Could not decode the file. Wrong encoding.")
try:
    x = 1
    print(x.upper())
except AttributeError:
    print('Error')
a = open('lesson8.txt')
data = a.read()
print(data)
a = open('lesson8.txt')
b = a.readlines(2)
print(b)

with open('lesson8.txt', 'a') as f :
    f.write('Learning Python is awesome')
filename = 'example.txt'
n = int(input("Enter number of lines to read from the end: "))

with open(filename, 'r') as file:
    lines = file.readlines()
    last_lines = lines[-n:]  # Get the last n lines
    for line in last_lines:
        print(line.strip())
filename = 'lesson8.txt'
with open (filename, 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]
print(lines)

with open('lesson8.txt','r') as f:
    lines = f.readlines()
    print(lines)
with open('lesson8.txt','r') as file:
    lines_array= [line.strip() for line in file]
print(lines_array)
with open ('lesson8.txt','r') as f :
    words = f.read().split()

longest= max(words, key=len)
print(longest)
with open('lesson8.txt', 'r') as f:
    line_count = len(f.readlines())
    print(line_count)
with open('lesson8.txt', 'r') as f :
    words = f.read().split()

freq ={}

for word in words:
    freq[word] = freq.get(word,0) + 1
print(freq)
import os

filename = 'lesson8.txt'

size = os.path.getsize(filename)
print(f"File size: {size} bytes")
open('destination.txt', 'w').write(open('source.txt').read())

with open('lesson8.txt', 'r') as source:
    content = source.read
with open('destination.txt', 'w') as destination:
    destination.write(content)
print("File copied successfully")

file1 = 'file1.txt'
file2 = 'file2.txt'
output_file = 'combined.txt'

# Open all files
with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as fout:
    # Read and combine lines one by one
    for line1, line2 in zip(f1, f2):
        combined_line = line1.strip() + ' ' + line2.strip() + '\n'
        fout.write(combined_line)
import random

# File name
filename = 'lesson8.txt'

# Read all lines into a list
with open(filename, 'r') as file:
    lines = file.readlines()

# Choose a random line
if lines:
    random_line = random.choice(lines)
    print("Random line:", random_line.strip())
else:
    print("The file is empty.")
# File name
filename = 'lesson8.txt'

# Open the file
file = open(filename, 'r')

# Check if the file is closed
print("Is file closed?", file.closed)  # Should be False

# Close the file
file.close()

# Check again
print("Is file closed after closing?", file.closed)  # Should be True
input_file = 'input.txt'
output_file = 'output.txt'

# Open input and output files
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        # Remove newline and write to output
        cleaned_line = line.strip()  # Removes \n and surrounding whitespace
        outfile.write(cleaned_line)

print(f"Newline characters removed. Clean content saved in '{output_file}'.")
