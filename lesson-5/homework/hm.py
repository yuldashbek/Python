def is_leap(year):
    return (year %4==0 and year %100 != 0) or (year % 400 ==0)
print(is_leap(2025))
print(is_leap(2024))

n= int(input("Enter a number: "))
if n % 2 !=0:
    print("weird")
elif 2<= n <= 5:
    print ("Not weird")
elif 6<= n <= 20 :
    print ("weird")
else :
    print ("Not weird")

a = int(input("Enter a: "))
b = int(input("Enter b: "))

even_numbers = list(range(a + a % 2, b + 1, 2)) if a % 2 == 1 else list(range(a, b + 1, 2))
print(even_numbers)

a = int(input("Enter a: "))
b = int(input("Enter b: "))

even_numbers = list(range(a + (a % 2), b + 1, 2))
print(even_numbers)
