import os

print(os.getcwd())         # текущая директория

print(os.path.exists('data.txt'))  # проверка существования пути (файла)
print(os.path.exists('data.tt'))  # проверка существования пути (файла)

print(os.path.isfile('data.txt'))  # проверка файл ли это
print(os.path.isfile(''))  # проверка файл ли это

abs_path=os.getcwd()
file_name='data.txt'
print(abs_path+'\\'+file_name)
print(os.path.join(abs_path,file_name))     # чтобф не париться со слэшэм

# список файлов папки
print(os.listdir("c:\\!!! Обучение Python.Basic"))

# полный (до самого дна) список файлов папки
for file in os.walk("c:\!!! Обучение Python.Basic"):
    print(file)




