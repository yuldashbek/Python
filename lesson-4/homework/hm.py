my_dict= {'a':1, 'b':2, 'c':3, 'd':4,}
asc = sorted(my_dict.items(), key=lambda x: x[1])
print("Ascending:",asc)
desc= sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
print("Descending:",desc)

sample_dict= {0: 10, 1: 20}
sample_dict.update({2: 30})
print(sample_dict)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {**dic1, **dic2, **dic3}
print(result)

n=5
result={}
for x in range(1,n+1):
    result[x]= x*x
print(result)

n=15
result={}
for x in range(1,n+1):
    result[x]= x*x
print(result)

myset ={"banana", "orange", "mango","apple"}
print(myset)
type(myset)

myset ={"banana", "orange", "mango","apple"}
for i in myset:
    print(i)

myset ={"banana", "orange", "mango","apple"}
add_set={"pineapple","onion"}

myset.update(add_set)
print(myset)

myset.remove("onion")
print(myset)

myset ={"banana", "orange", "mango","apple"}
if "pepper" in myset:
    myset.remove('perrer')
else :
    print('No item in set')
  
