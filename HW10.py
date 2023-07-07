from collections import UserDict


class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)
   
    
class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        
        
class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        
        
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]
        
    def change_phone(self, old_phone, new_phone):   # створив метод для зміни номеру. Спробую додати зміну за ім'ям  в класі AddressBook   
        for i, phone in enumerate(self.phones):
            if str(phone) == str(old_phone):
                self.phones[i] = new_phone
                break

    def __str__(self):
        return f"Name: {self.name}, Phones: {', '.join(str(p) for p in self.phones)}"  #я не впевнений чи потрібен нам тут ось цей метод для перетворення в рядок чи без нього буде просто запис що це класс комірка така то типу клас такий то ? трошки заплутався але зробив по аналогії з вашим прикладом в class Seat (приклад з квитками на футбол). 
    
    
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[str(record.name)] = record

    def remove_record(self, name):
        del self.data[str(name)]

    def search_by_name(self, name):
        results = []
        for record in self.data.values():
            if str(record.name) == name:
                results.append(record)
        return results
    
    def change_phone_by_name(self, name, new_phone):  # намагаюсь зробити метод зміни номеру за імʼям
        results = self.search_by_name(name)
        for result in results:
            result.change_phone(result.phones[0], Phone(new_phone))

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
    
if __name__ == "__main__":  
    # створюю записи
    record1 = Record("Bill")
    record1.add_phone("123456789")
    record1.add_phone("987654321")

    record2 = Record("Joan")
    record2.add_phone("111222333")

    # Створення адресної книги з обʼєктами record (з нашими записами створеними вище)
    address_book = AddressBook()
    address_book.add_record(record1)
    address_book.add_record(record2)

    # Пошук за ім'ям
    results = address_book.search_by_name("Bill")
    for result in results:
        print(result)

    # Видалення запису
    address_book.remove_record("Bill")
    
    # Зміна номеру в записі
    # record2.change_phone(Phone("111222333"), Phone("111222000"))
    
    # Зміна номеру за імʼям 
    address_book.change_phone_by_name("Joan", "123000999")

    # Друк всієї адр книги
    print(address_book)