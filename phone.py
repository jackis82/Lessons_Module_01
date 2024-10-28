import json
import os

class Contact:
    def __init__(self, first_name, last_name, phone_number, company=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.company = company

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f'{self.full_name}: {self.phone_number}'

        
class PhoneBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        try:
            with open(self.filename, 'r') as f:
                self.contacts = json.load(f)
        except FileNotFoundError:
            self.contacts = []

            print(f'Файл {self.filename} не найден, создаётся пустой список.')

            
    def save_to_file(self):
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=4)

    def add_contact(self):
        first_name = input("Введите имя: ")
        last_name = input("Введите фамилию: ")
        phone_number = input("Введите номер телефона: ")
        company = input("Введите название компании: ")

        contact = Contact(first_name, last_name, phone_number, company)
        self.contacts.append(contact)
        self.save_to_file()
        print(f"Контакт {contact.full_name} добавлен в телефонную книгу.")

    def find_by_phone(self):
        phone_number = input("Введите номер телефона: ")
        results = [contact for contact in self.contacts if contact.phone_number == phone_number]
        if len(results) > 0:
            print(f"Контакт с номером {phone_number}: {results[0].full_name}")
        else:
            print(f"Нет контакта с таким номером.")

    def list_contacts(self):
        contacts = sorted(self.contacts, key=lambda c: c.last_name)
        for contact in contacts:
            print(contact)

    def delete_contact(self):
        phone_number = input("Введите номер телефона: ")
        contacts = [contact for contact in self.contacts if contact.phone_number != phone_number]
        if len(self.contacts) == len(contacts):
            print(f"Не найдено контактов с номером {phone_number}.")
        else:
            self.contacts = contacts
            self.save_to_file()
            print(f"Удалено {len(self.contacts) - len(contacts)} контактов.")

    def modify_contact(self):
        phone_number = input("Введите номер телефона: ")
        contacts = [contact for contact in self.contacts if contact.phone_number == phone_number]
        if len(contacts) > 0:
            contact = contacts[0]
            new_first_name = input(f"Новый номер телефона для {contact.full_name}: ")
            contact.first_name = new_first_name
            contact.last_name = input("Новая фамилия: ")
            contact.phone_number = input("Новый номер телефона: ")
            contact.company = input("Название компании: ")
            self.save_to_file()
            print(f"Контакт {contact.full_name} изменен.")
        else:
            print(f"Не найдено контактов с номером {phone_number}.")

def main():
    pb = PhoneBook()

    while True:
        print("\nМеню:")
        print("1. Посмотреть все контакты")
        print("2. Найти контакт по телефону")
        print("3. Добавить контакт")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Сохранить изменения и выйти")

        choice = int(input("Ваш выбор: "))

        if choice == 1:
            pb.list_contacts()
        elif choice == 2:
            pb.find_by_phone()
        elif choice == 3:
            pb.add_contact()
        elif choice == 4:
            pb.modify_contact()
        elif choice == 5:
            pb.delete_contact()
        elif choice == 6:
            pb.save_to_file()
            break

if __name__ == "__main__":
    main()