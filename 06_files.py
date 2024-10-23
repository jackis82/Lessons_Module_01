path='data.txt'
data_file=open(path,'r',encoding='utf-8')
print(type(data_file))
print(data_file)

# for line in data_file:
#     print(line)
# for line in data_file:
#     print(line.__repr__())

# data=data_file.read()
# print(data)

data=data_file.readline()

# данные в виде списка строк:
# data=data_file.readlines()
# print(data)
# for r in data:
#     print(r.__repr__())

# данные в виде списка строк и распиленные по \n:
data=data_file.read().split('\n')
# для того чтобы убрать лишние пробелы и табуляции и др. в начале и в конце каждого элемента списка
data=list(map(lambda x: x.strip(),data))
print(*data,sep='\n')

# для закрытия файла
# data_file.close()
# вместо можно использовать контекстный менеджер
# (как только из него выйдем, то файл авто-ки закрывается):
with open(path,'r',encoding='utf-8') as data_file2:
    data=data_file2.readlines()
    data = list(map(lambda x: x.strip(), data))
    print(*data, sep='\n')


# w - запись (write); r - чтение (read); a - добавлять в конец (append)
with open(path,'a',encoding='utf-8') as data_file:
    new_contact='Оганес Симонян; 888; хранитель'
    data_file.write('\n'+new_contact)

print('\n\nand:')

with open(path,'r',encoding='utf-8') as data_file:
    print(data_file.tell())     # положение каретки при чтении
    data_file.seek(4)
    data=data_file.readline()
    print(data_file.tell())

print(data+'\n')


