my_set={1,2,3,4}
print(my_set)
print(type(my_set))

my_set={'1','2','3','4'}
print(my_set)

my_set={1,2,2,3,4,4}
print(my_set)

# удаляем ненужные дубликаты из списка, с помощью преобразования в set и обратно в list
print('\nудаляем ненужные дубликаты из списка, с помощью преобразования в set и обратно в list:')
my_list =[1,2,2,3,4,4]
print(my_list)
my_list=list(set(my_list))
print(my_list)

# пересечение множеств:
print('\nпересечение множеств:')
set_a={1,2,3,6}
set_b={2,3,4,5}
print(set_a)
print(set_b)
print(set_a.intersection(set_b))
# данная строка изменит множество (возвращает результат)
set_a.intersection_update(set_b)
# set_a=intersection(set_b)   тождественно  set_a.intersection_update(set_b)
print(set_a)


# отличие множеств (a от b):
set_a={1,2,3,6}
print('\nотличие множеств (a от b):')
set_a={1,2,3,6}
set_b={2,3,4,5}
print(set_a.difference(set_b))

# объединение множеств (a и b):
print('\nобъединение множеств (a и b):')
print('set_a=',set_a)
print('set_b=',set_b)
print(set_a.union(set_b))


#  добавление и удаление элемента из множества:
print('\nдобавление и удаление элемента из множества:')
print('set_a=',set_a)
set_a.add(7)
print('set_a=',set_a)
set_a.remove(6)
print('set_a=',set_a)


#  pop - возвращает 1-й элемент (1-й хеш):
print('\npop - возвращает 1-й элемент (1-й хеш):')
print(set_a.pop())

#  проверка вхождения элемента в множество:
print('\nпроверка вхождения элемента в множество:')
print(1 in set_b)
print(2 in set_b)

#  очищение множества:
print('\nочищение множества:')
set_b.clear()
print(set_b)


