import json

def check_opened():
    global opened
    global ph_list
    global max_fio_length
    if opened == 0:
        ph_list = read_contacts(path)
        max_fio_length = get_max_fio_length()
        opened = 1
        print('Справочник открыт')

def print_continue():
    print('--- для продолжения нажмите Enter ---')
    input()
    print_menu(0)


# функция отображает меню
def print_menu(n: int) -> int:
    global opened
    global ph_list
    global sel_contact

    if n == 0:
        print('МЕНЮ:')
        print('-------------------------------------------')
        print('1. Открыть справочник...')
        print('2. Показать все контакты...')
        print('3. Выбрать контакт по индексу...')
        print('4. Показать данные выбранного контакта...')
        print('5. Найти контакт...')
        print('6. Создать контакт...')
        print('7. Изменить контакт...')
        print('8. Удалить контакт...')
        print('9. Сохранить данные...')
        print('0. ВЫХОД')
        print('-------------------------------------------')
        print('')
        n = input('ВЫБЕРИТЕ ПУНКТ МЕНЮ: ')
        while not n.isdigit():
            n = input('ВЫБЕРИТЕ ПУНКТ МЕНЮ: ')
        n_menu = int(n)

    else:
        n_menu = int(n)

    print('n_menu='+str(n_menu))
    print(type(n_menu))
    # 1. Открыть справочник...
    if n_menu == 1:
        path = 'phonedir.json'
        print('1. Открыть справочник')
        if opened:
            print('Справочник уже открыт.')
            if input('Открыть его заново (y - ДА)? '):
                check_opened()
        else:
            check_opened()
            print('Справочник открыт')
        print_continue()

    # 2. Показать все контакты...
    if n_menu == 2:
        check_opened()
        print('перед выводом:')
        print_all_contacts(1, 1, 1)
        print_continue()


    # 3. Выбрать контакт по индексу...
    if n_menu == 3:
        check_opened()
        p = input('Введите порядковый номер контакта'
                  '(для возврата нажмите Enter): ')
        if p:
            if p.isdigit():
                # print('p.isdigit')
                # print(type(p))
                p = int(p)
                # print(f'p={p}')
                # print('len='+len(ph_list))
                if (p>0) & (p<=len(ph_list)):
                    sel_contact = select_contact(p-1)
                    print('Выбран контакт:')
                    print_contact(sel_contact, 1, 1, 0)
                    print_continue()
                else:
                    print('Порядковый номер за пределами справочника!')
                    print('')
                    print_menu(3)
            else:
                print_menu(3)
        else:
            print_continue()


    # 4. Показать данные выбранного контакта...
    if n_menu == 4:
        if sel_contact == {}:
            print('Нет выбранного котакта!')
            print_menu(3)
            print_menu(4)
        else:
            print_contact(sel_contact, 1, 1, 1)
            print_continue()


    # 5. Найти контакт...')
    # 6. Создать контакт...')
    # 7. Изменить контакт...')
    # 8. Удалить контакт...')
    # 9. Сохранить данные...')




# функция чтения из json-файла контактов в список
def read_contacts(path: str) -> list:
    # открываем файл
    with open(path, 'r', encoding='utf-8') as json_file:
        contacts_list = json.load(json_file)
        return contacts_list

# функция сохранения в json-файл контактов из списка
def save_contacts(path: str, a_list):
    # открываем файл
    for a_dict in a_list:
        a_dict.pop('номер')
        a_dict.pop('ФИО')

    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(a_list, json_file, indent=4, ensure_ascii=0)  # ensure_ascii=0 - для записи кириллицы
        # for i in range(len(a_list)):
        #     el_dict = a_list[i]
        #     print(type(el_dict))
        #     print(el_dict)
        #     json.dump(el_dict, json_file, indent=4, ensure_ascii=0)


# print(type(ph_list))       # тип словарь
# print(ph_list[0])
# print(type(ph_list[0]))       # тип словарь

# el_dict=ph_list[0]

# el_dict['ФИО']=el_dict.get('Фамилия','')+' '+el_dict.get('Имя','')+' '+el_dict.get('Отчество','')
# print(el_dict['ФИО'])



# функция определяет макс.длину ФИО контакта
def get_max_fio_length() -> int:
    global opened
    global ph_list
    global sel_contact

    max_fio_length=0
    # поиск max_fio_length (для дальнейшего выравнивания вывода списка)
    for i in range(len(ph_list)):
        el_dict=ph_list[i]
        el_dict['номер']=i+1
        el_dict['ФИО'] = el_dict.get('Фамилия', '') + ' ' + el_dict.get('Имя', '') + ' ' + el_dict.get('Отчество', '')
        if max_fio_length<len(el_dict['ФИО']):
            max_fio_length=len(el_dict['ФИО'])
    return max_fio_length
    # print(f'max_fio_length={max_fio_length}')




# функция печатает информацию обо всех контактах
def print_all_contacts(print_num=1,print_fio=1,print_tel_comp=0):
    global opened
    global ph_list
    global sel_contact

    for i in range(len(ph_list)):
        el_dict=ph_list[i]
        # el_dict['ФИО'] = el_dict.get('Фамилия', '') + ' ' + el_dict.get('Имя', '') + ' ' + el_dict.get('Отчество', '')
        # print(el_dict['ФИО'])

        fio=el_dict['ФИО']
        tel_comp = el_dict['Телефон'] + ' (' + el_dict['Компания'] + ')'

        output_str = ''
        if print_num:
            output_str+=(i+1).__str__()+') '
        if print_fio:
            output_str+=fio
        if print_tel_comp:
            str_spaces = ''
            if print_fio & print_tel_comp:
                # определяем кол-во пробелов между ФИО и номером (для выравнивания)
                tt = max_fio_length - len(fio)
                # print(tt)
                for k in range(tt):
                    str_spaces += ' '

            output_str+=str_spaces+f'\t\t{tel_comp}'
        print(output_str)


def select_contact(n: int):
    global ph_list
    return ph_list[n]



# функция печатает информацию о контакте
def print_contact(a_dict,print_num=1,print_fio=1,print_tel_comp=0):
    fio = a_dict['ФИО']
    tel_comp = a_dict['Телефон'] + ' (' + a_dict['Компания'] + ')'

    output_str = ''
    if print_num:
        output_str += str(a_dict['номер']) + ') '
    if print_fio:
        output_str += fio
    if print_tel_comp:
        str_spaces = ''
        if print_fio & print_tel_comp:
            # определяем кол-во пробелов между ФИО и номером (для выравнивания)
            tt = max_fio_length - len(fio)
            # print(tt)
            for k in range(tt):
                str_spaces += ' '

        output_str += str_spaces + f'\t\t{tel_comp}'
    print(output_str)

# функция обновляет параметр контакта и
# возвращает 1, если значение изменилось (иначе 0)
def update_value(a_dict, var_cap, var_str):
    new_value = input(f"Введите новое значение ({var_cap}, текущее значение: '{var_str}') или нажмите Enter, чтобы оставить прежнее: ")
    if new_value:
        a_dict[var_cap]=new_value
        return 1
    else:
        return 0

# функция оставляет в строке только цифры (остальное удаляет)
def extract_digits(input_str) -> str:
    # result = ''.join(char for char in input_str if char.isdigit())
    res = ''
    for char in input_str:
        if char.isdigit():
            res +=char
    return res




# функция добавляет контакт
def append_contact() -> dict:
    global ph_list

    print('Введите данные нового контакта:')
    new_f = input('Введите Фамилию: ')
    if new_f:
        new_i = input('Введите Имя: ')
        new_o = input('Введите Отчество: ')
        new_tel = input('Введите номер телефона: ')
        if new_tel:
            new_dict = {}
            new_dict['Фамилия'] = new_f
            new_dict['Имя'] = new_i
            new_dict['Отчество'] = new_o
            new_dict['Телефон'] = new_tel

            new_comp = ''
            new_comp = input('Введите название компании: ')
            new_dict['Компания'] = new_comp
            # new_dict['Компания'] = new_comp

    ph_list.append(new_dict)
    get_max_fio_length()
    print(f'Контакт  добавлен')
    return new_dict



# функция удалаяет контакт с индексом n
def delete_contact(n: int):
    global ph_list

    el_dict = ph_list[n]
    fio = el_dict['ФИО']
    print(f'Вы уверены, что нужно удалить контакт {fio}?')
    if input('Нажмите "y", если нужно удалить...'):
        ph_list.pop(n)
        print(f'Контакт {fio} удалён')


# функция изменяет контакт
def change_contact(a_dict) -> dict:
    print(f'\tдля изменения ФИО введите "f"')
    print(f'\tдля изменения ТЕЛЕФОНА введите "t"')
    print(f'\tдля изменения КОМПАНИИ введите "k"')
    print(f'\tдля ВЫХОДА введите "0"')

    inp_char = input(f'\t\tВаш выбор? ')
    if inp_char=='f':
        t_f = update_value(a_dict,'Фамилия', a_dict['Фамилия'])
        t_i = update_value(a_dict,'Имя', a_dict['Имя'])
        t_o = update_value(a_dict,'Отчество', a_dict['Отчество'])
        a_dict['ФИО'] = a_dict.get('Фамилия', '') + ' ' + a_dict.get('Имя', '') + ' ' + a_dict.get('Отчество', '')
        print(f't_f={t_f} t_i={t_i} t_o={t_o} ')

        if t_f | t_i | t_o:
            print('Новое значение: '+a_dict['ФИО'])

    if inp_char=='t':
        t_t = update_value(a_dict,'Телефон', a_dict['Телефон'])
        if t_t:
            print('Новое значение: ' + a_dict['Телефон'])
    if inp_char=='k':
        t_k = update_value(a_dict,'Компания', a_dict['Компания'])
        if t_k:
            print('Новое значение: ' + a_dict['Компания'])
    return a_dict


# функция ищет контакт по ФИО и
# возвращает номер элемента в списке (иначе -1)
def find_contact_fio(fio_to_find: str) -> int:
    global ph_list

    print('\nИщем ' + fio_to_find + '...')
    res = -1
    for i in range(len(ph_list)):
        el_dict=ph_list[i]
        el_dict['ФИО']=el_dict.get('Фамилия', '') + ' ' + el_dict.get('Имя', '') + ' ' + el_dict.get('Отчество', '')
        # print(el_dict['ФИО'])
        fio_lower=el_dict['ФИО'].lower()
        if fio_lower.find(fio_to_find)>-1:
            res=i
            break
    return res
        # return None

# функция ищет контакт по телефону и
# возвращает номер элемента в списке (иначе -1)
def find_contact_tel(tel_to_find: str) -> int:
    global ph_list

    print('\nИщем ' + tel_to_find + '...')
    res = -1
    for i in range(len(ph_list)):
        el_dict=ph_list[i]
        tel_digits=extract_digits(el_dict['Телефон'])
        if tel_digits.find(extract_digits(tel_to_find))>-1:
            res=i
            break
    return res


# функция ищет контакт по компании и
# возвращает номер элемента в списке (иначе -1)
def find_contact_comp(comp_to_find: str) -> int:
    global ph_list

    print('\nИщем ' + comp_to_find + '...')
    res = -1
    for i in range(len(ph_list)):
        el_dict=ph_list[i]
        tel_digits=extract_digits(el_dict['Компания'])
        if tel_digits.find(extract_digits(comp_to_find))>-1:
            res=i
            break
    return res



path='phonedir.json'
new_path='phonedir_2.json'

opened = 0
ph_list=[]
sel_contact={}

print('-------- Телефонный справочник, версия 1.0 --------')
print_menu(0)


# ph_list=read_contacts(path)
# max_fio_length=get_max_fio_length()

# print_all_contacts(1,1,1)
# sel_contact=select_contact(50)
# print('\nВыбран контакт:')
# print_contact(sel_contact,1,1,1)

# tel_digits = extract_digits('903-456-78')
# print(tel_digits)
# f_n = find_contact_tel('903-456-78')
# sel_contact=select_contact(f_n)

# print('\nНайден контакт:')
# print_contact(sel_contact,1,1,1)

# append_contact()
# change_contact(sel_contact)
# print_all_contacts(1,1,1)
# delete_contact(f_n)
# save_contacts(new_path, ph_list)

# print('\nПоиск по ФИО:')
# fio_to_find=input('Введите, кого найти: ').lower()
# res=find_contact_fio(fio_to_find)
# if (res>=0):
#     print_contact(ph_list[res])
#     # print(ph_list[res])
#     # print(*ph_list[res],sep='\n')       # * - распаковывает коллекцию на элементы
# else:
#     print('Ничего не найдено')
#

