name= input('Enter your name:')
year= int(input('Enter you birthyear'))
from datetime import datetime
current_year=datetime.now().year
age= current_year - year
print("Hello", name + "!", "You are", age, "years old.")

txt = 'LMaasleitbtui'
txt[::2]
txt[1::2]

txt = 'MsaatmiazD'
txt[::2]
txt[::-2]

txt = "I'am John. I am from London"
txt[21::]

user_input= input("Enter a string: ")
reversed_string= user_input[::-1]
reversed_string

text= input("Enter a string:")
count= 0 
for char in text:
    if char.lower() in "uioae":
        count +=1
print("Number of vowels:", count)

numbers_input = input("Enter a list of numbers separated by spaces: ")
numbers= list(map(float,numbers_input.split()))
if numbers: 
    max_value= max(numbers)
    print("The maximum value is:", max_value)
else:
    print("No numbers were entered.")

st =input("Enter text:")
if (st == st[::-1]):
    print("This a Palindrome")
else :
    print("This is not Palindrome")

email = "user@example.com"
domain = email.split('@')[1]
print(domain)
