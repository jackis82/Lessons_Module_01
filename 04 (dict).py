# словарь из элементов 'ключ':значение
my_dict={'one':1,'two':2,'three':3}
print(my_dict)
print(type(my_dict))

# пустой словарь:
empty_d={}
# или:
# empty_d=dict()
# пустое множество
empty_s=set()


# все объекты в куче
# for i in globals().copy().items():
#     print(i)
my_dict['four']=4
print(my_dict)
my_dict['four']=5
print(my_dict['three'])

# получить элемент по ключу
print(my_dict.get('three','no datas'))
print(my_dict.get('thee','no datas'))


# удалить элемент по ключу
print(my_dict.pop('one'))
print(my_dict)

# обновление словаря данными из другого
n_dict={'one':13,'two':24,'three':113}
print(n_dict)
n_dict.update(my_dict)
print(n_dict)


# безопасное удаление нового ключа (добавится только если ключа нет)
print(n_dict)
n_dict.setdefault('thee',333)
print(n_dict)

# переопределение словаря
n_dict={}.fromkeys('ABCDEF',None)
print(n_dict)

for item in my_dict.keys():
    print(item)
for item in my_dict.values():
    print(item)
for key,value in my_dict.items():
    print(f'{key} ={value}')

# dict_item=my_dict.items()
# for item in dict_item:
#     for key,value in item:
#         print(f'{key} ={value}')
#     print(type(item))


keys=[1,2,5,4]
my_t=(7,8,9,0)

print('keys and tuple:')
for i in range(len(keys)):
        print(keys[i])
        print(my_t[i])

