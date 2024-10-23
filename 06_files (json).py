import json

path='data.json'
json_data={
    'one-1':'один',
    'two-2':'два',
    'three-3':'три',
    'four-4':'четыре'
}

# with open(path,'w',encoding='utf-8') as json_file:
#     json.dump(json_data,json_file,indent=4,ensure_ascii=0)    # ensure_ascii=0 - для записи кириллицы
# with open(path,'a',encoding='utf-8') as json_file:
#     json.dump(json_data,json_file,indent=4,ensure_ascii=0)    # ensure_ascii=0 - для записи кириллицы

# чтобы добавить в json, нужно прочитать данные в словарь, добавить данные в словарь, а затем перезаписать json-файл
with open(path,'r',encoding='utf-8') as json_file:
    data=json.load(json_file)
data['five']='пять'
# data[4]='четыре'   - !! иметь ввиду что в json-файле все ключи - строчные, т.е. при записи в файл int преобразуется в str
with open(path,'w',encoding='utf-8') as json_file:
    json.dump(data,json_file,indent=4,ensure_ascii=0)    # ensure_ascii=0 - для записи кириллицы

with open(path,'r',encoding='utf-8') as json_file:
    data=json.load(json_file)

print(data)
print(type(data))       # тип словарь
