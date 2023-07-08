from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
   
    
class Name(Field):
    pass
        
        
class Phone(Field):
    pass
        
        
class Record:
    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phones = []
        if phone is not None:
            self.add_phone(phone)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]
        
    def change_phone(self, old_phone, new_phone):   
        for i, phone in enumerate(self.phones):
            if str(phone) == str(old_phone):
                self.phones[i] = new_phone
                break

    def __str__(self):
        return f"Name: {self.name}, Phones: {', '.join(str(p) for p in self.phones)}" 
    
    
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
    
    def change_phone_by_name(self, name, new_phone):  
        results = self.search_by_name(name)
        for result in results:
            result.change_phone(result.phones[0], Phone(new_phone))

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
    
if __name__ == "__main__":
    
    ab = AddressBook()
    name = Name("Bill")
    phone1 = Phone("12345")
    rec = Record(name, phone1)
    print(rec.name)
    
    ab.add_record(rec)
    
    ab.add_record(Record(Name("Jill")))
    
    for rec in ab.values():
        assert isinstance(rec, Record)
    
    phone2 = Phone("56784")
    print(ab)
        
    rec = ab["Jill"]
    print(rec)
    
    rec.add_phone(phone2)
    print(rec)
    
    ab.add_record(Record(Name("Jerry")))
    phone3 = Phone("488447474")
    rec = ab["Jerry"]
    rec.add_phone(phone3)
    
    rec.change_phone(Phone("488447474"), Phone("99345"))
    
    print(ab)
    
   