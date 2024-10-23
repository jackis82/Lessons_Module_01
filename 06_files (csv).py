import csv
from dataclasses import dataclass

path='data.csv'

# чтение из csv-файла в data
with open(path,'r',encoding='utf-8') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=';')
    data=[]
    for row in csv_reader:
        # print(row)
        data.append(row)

# новые данные
new_data=['Тиурин А.А.','789415123','кто-то']
print(*data,sep='\n')       # * - распаковывает коллекцию на элементы

# добавляем данные в csv-файл
with open(path,'a',encoding='utf-8') as csv_file:
    csv_writer=csv.writer(csv_file,delimiter=';')
    csv_writer.writerow(new_data)


# добавляем в data данные
data.append(['Тиурин А.А,','789415123','кто-то'])

headers=['ФИО','телефон','профессия']
# добавляем данные в csv-файл
with open(path,'w',encoding='utf-8') as csv_file:
    csv_writer=csv.writer(csv_file,delimiter=';',lineterminator='\n')
    csv_writer.writerow(headers)    # запись заголовков в файл
    csv_writer.writerows(data)

print(*data,sep='\n')       # * - распаковывает коллекцию на элементы
