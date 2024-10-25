my_tuple=(1,2,3,4,5)
# или можно так
my_tuple=1,2,3,4,5

# так не работает:
# my_tuple[2]='A'

print(my_tuple)
print(type(my_tuple))
print(my_tuple[3])

my_tuple=(1,1,3,4,5,[11,12,13])
print(my_tuple)
print(my_tuple.index(1))
print(my_tuple[-1].append((6)))
print(my_tuple)
# - но кортеж может хранить только неизменяемые объекты (ссылки на них), а список - изменяемый
print(my_tuple.count(1))

#  кортеж из одного элемента
#  если объявить (1), то при обращении к о-му элементу будет ошибка
n_tuple=(1,)
print(n_tuple)
print(n_tuple[0])

