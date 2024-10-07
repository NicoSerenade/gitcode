# class Library():
#     def __init__(self, name):
#         self.name = name
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def list_books(self):
#         return [f'{book.title} by {book.author}' for book in self.books]

# class Book():
#     def __init__(self, name, author):
#         self.title = name
#         self.author = author

# library = Library('Nico\'s library')

# book1 = Book('Deepwork','cal')
# book2 = Book('beyond chaos','peterson')
# book3 = Book('power of now','eckhart')

# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# # print(library.list_books())

# class Engine():
#     def __init__(self, horse_power):
#         self.horse_power = horse_power

# class Wheel():
#     def __init__(self, size):
#         self.size = size

# class Car():
#     def __init__(self, make, model, horse_power, wheel_size):
#         self.make = make
#         self.model = model
#         self.engine = Engine(horse_power)
#         self.wheels = [Wheel(wheel_size) for wheel in range(4)]

#     def display_car(self):
#         print(f'{self.make} {self.model} {self.engine.horse_power} {self.wheels[0].size}')

# car1 = Car('ford', 'fiesta', 500, 18)

# car1.display_car()

# class Company():
#     class Employee():
#         def __init__(self, name, position):
#             self.name = name
#             self.position = position
        
#         def get_details(self):
#             return f'{self.name} {self.position}'
        
#         @staticmethod
#         def is_valid_position(position):
#             valid_positions = ['supp', 'adc', 'jg']
#             return position in valid_positions

#     def __init__(self, company_name):
#         self.company_name = company_name
#         self.employees = []

#     def add_employee(self, name, position):
#         new_employee = self.Employee(name, position)
#         self.employees.append(new_employee)

#     def list_employees(self):
#         return [trabajador.get_details() + ' for ' + self.company_name for trabajador in self.employees]
    
# company1 = Company('diostebendiga')

# company1.add_employee('Farlan', 'farmer')
# company1.add_employee('Fernando', 'manager')
# company1.add_employee('Rossy', 'gardener')

# company2 = Company('nicolas castaneda')

# company2.add_employee('Nicolas', 'Manager')
# company2.add_employee('Valen', 'Musician')
# company2.add_employee('Juank', 'biologist')

# for employee in company1.list_employees():
#     print(employee)

# print('\nvs\n')

# for employee in company2.list_employees():
#     print(employee)

# print(Company.Employee.is_valid_position('jg'))

# class Book():

#     books = []

#     def __init__(self, name, author, pages):
#         self.name = name
#         self.author = author
#         self.pages = pages

#     @classmethod
#     def add_book(cls, book):
#         Book.books.append(book)

#     def __str__(self):
#         return f'{self.name} By {self.author}, {self.pages} pages.'
    
#     def __eq__(self, other):
#         return self.name == other.name and self.author == other.author
    
#     def __lt__(self, other):
#         return self.pages < other.pages
    
#     def __gt__(self, other):
#         self_rank = 1 if self.name == 'El Pepe' else 2 if self.name == 'Sun Tzu' else 3
#         other_rank = 1 if other.name == 'El Pepe' else  2 if other.name == 'Sun Tzu' else 3
        
#         return self_rank < other_rank
    
#     def __add__(self, other):
#         return 'colaboration between ' + self.author + ' and ' + other.author 
    
#     def __contains__(self, keyword):
#         return keyword in self.name or keyword in self.author
    
#     def __getitem__(self, key):
#         return self.author if key == 'carro' else None
    
# book1 = Book('The art of war1', 'Sun Tzu', 1000)
# book2 = Book('The art of war1', 'El Pepe', 1500)
# book3 = Book('The art of war2', 'Sun Tzu', 900)
# book4 = Book('The art of war3', 'Sun Tzu Jr', 1000)

# Book.add_book(book1)
# Book.add_book(book2)
# Book.add_book(book3)
# Book.add_book(book4)

# for libro in Book.books:
#     print(libro)

# print(book1 == book1)

# print(book1 < book3)

# print(book2 > book4)

# print(book1 + book2)

# print('Pepe' in book2)

# print(book2.author)

# print(book2['carro'])


class BankAccount():
    def __init__(self, name, balance):
        self._name = name
        self.balance = balance
    
    @property
    def name(self):
        return f'{self._name} is the owner'
    
    @name.setter
    def name(self, new_owner):
        if new_owner != self._name:
            self._name = new_owner
        else:
            print(self._name, 'is the current owner')

    @name.deleter
    def name(self):
        del self._name
        print('The owner has been deleted')
    
account1 = BankAccount('Laura', 1000)



account1.name = 'Lauro'

print(account1.name)
    
del account1.name