fruits=['apple','banana','orange','mango','cherry']
print(fruits[2])

number1=[1,2,3,4,5]
number2=[6,7,8,9,10]
number1.extend(number2)
print(number1)

numbers=[1,2,3,4,5]
print([numbers[i] for i in (0,2,4)])

movies=['borat','farsaj','dictator','mrbean','friend']
movies_tuple= tuple(movies)
print(movies_tuple)
type(movies_tuple)

cities= ['Tashkent','Moscow','Paris','London','New York']
if 'Paris' in cities:
    print('yes.Paris in the list of cities')
else:
    print('No. Paris in not in the list of cities')

numb= [1,2,3,4,5,6,7,8,9,10]
dublicated= numb*2
print(dublicated)

numb= [1,2,3,4,5,6,7,8,9,10]
numb[0],numb[-1] = numb[-1],numb[0]
print(numb)

numbers =(1,2,3,4,5,6,7,8,9,10)
print(numbers[3::])

colours= ['red','blue','orange','yellow','green','blue','white','blue']
colours.count('blue')

animals=('panda','rabbit','wolf','lion','eagle')
animals.index('lion')

number1=(1,2,3,4,5)
number2=(6,7,8,9,10)
merged_tuple= number1 + number2
print(merged_tuple)

numb= [1,2,3,4,5,6,7,8,9,10]
len(numb)


numbers= (1,2,3,4,5)
numbers= list(numbers)
print(numbers)
type(numbers)


numb= (1,2,3,4,5,6,7,8,9,10)
max(numb)
min(numb)

animals=('panda','rabbit','wolf','lion','eagle')
reversed_animals= animals[::-1]
print(reversed_animals)

