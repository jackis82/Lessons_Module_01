import random

nums=list('6184375')
lets=list('abcdefghij')
# print(nums)
random.shuffle(nums)
# print(nums)
random.shuffle(lets)
my_list=[(int(nums[i]),lets[i]) for i in range(len(nums))]
print(my_list)
print(sorted(my_list, key=lambda x: x[0]))  # сортировать по цифре
print(sorted(my_list, key=lambda x: x[1]))  # сортировать по букве


data=list('1234454576')
print(data)

for i in range(len(data)):
    data[i]=int(data[i])
# этому равносильно применение lambda-функции:

# map и filter - функции высшего порядка (в качестве ее аргумента может быть другая функция)

# пример применения map с lambda - возведение в квадрат
data=list(map(int,data))              # каждый элемент преобразуется в int

data=list(map(lambda x: x*3,data))    # каждый элемент умножается на 3
print(data)

# еще пример применения lambda - возведение в квадрат
print((lambda x: x**2)(12))

# # пример применения filter с lambda
data=list(filter(lambda x: int(x)%2,data))    # в результат добавляется элемент, если выполняется условие "int(x)%2" (только нечетные элементы)
print(data)
data=list(filter(lambda x: int(x)>10,data))    # в результат добавляется элемент, если элемент > 10
print(data)


# функция zip
numbers=(1,2,3,4,5,6,7)
letters='a','b','c'
puncts=('!@#$%')

print(list(zip(numbers, letters)))
print(list(zip(numbers, letters,puncts)))   # только 3 элемента

from itertools import zip_longest
print(list(zip_longest(numbers, letters,puncts)))   # все 5 элементов
print(list(zip_longest(numbers, letters,puncts,fillvalue='000')))   # все 5 элементов но без None


print('')
my_list=[]
for i in range(20):
    if i%2:
        my_list.append(i**2)
print(my_list)

# но вместо этого можно воспользоваться списковым включением (одна строка):
my_list=[i**2 for i in range(20) if i%2]    # затирает список новыми значениями
print(my_list)
my_list=[i+100 for i in range(20)]          # затирает список новыми значениями
print(my_list)




