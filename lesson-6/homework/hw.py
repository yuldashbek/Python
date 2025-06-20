def insert_underscores(txt):
    result = ""
    count = 0
    i = 0

    while i < len(txt):
        result += txt[i]
        count += 1

        if count == 3:
           
            if txt[i] not in 'aeiouAEIOU' and (i + 1 >= len(txt) or txt[i + 1] != '_'):
                result += "_"
            count = 0
        i += 1

    if result.endswith("_"):
        result = result[:-1]

    return result


print(insert_underscores("hello"))           
print(insert_underscores("assalom"))        
print(insert_underscores("abcabcabcdeabcdefabcdefg")) 

n=int(input())
for i in range(n):
    print(i** 2)

i=1
while i <= 10:
    print(i)
    i= i+1

for i in range(1,6):
    for j in range(1,i + 1):
        print(j, end=" ")
    print()

n= int(input("Enter number: "))
total= 0
for i in range(1, n+1):
    total += i
print ("sum is:", total) 

n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 70 <= num <= 160:
        print(num)

num = input("Enter a number: ")
print("total digits:", len(num))

i = 5
while i >= 1 :
    j = i
    while j >= 1:
        print(j, end=" ")
        j -= 1 
    print()
    i -= 1

list1 = [10, 20, 30, 40, 50]
for i in range(len(list1)-1, -1, -1):
    print(list1[i])
for num in reversed(list1):
    print(num)

for i in range(-10,0):
    print(i)
i = -10
while i < 0:
    print(i)
    i += 1

i = 0
while i < 5:
    print(i)
    i = i + 1
print("Done")

for num in range(25, 51):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

a = 0 
b = 1

for i in range(10):
    print(a, end =" ")
    a,b = b, a + b 

num = int(input("Enter a number to find factorial: "))
factorial = 1
for i in range(1, num +1):
    factorial *= i
print(f"{num}! = {factorial}")

list2 = [2, 3, 4]
result = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
print(result)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
print(result)

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
result= [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
print(result)
