# Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()


class Circle:
    radius: float = None
    color: str = None

    def __init__(self, radius, colors):
        self.radius = radius
        self.colors = colors

    def circle_description(self):
        print(f'The radius of the circle is {self.radius}, and the color is {self.colors}.')

    def circle_area(self, pi_value=3.14159):
        print(f'The area of the circle is: {format(float(pow(self.radius, 2) * pi_value), "2f")}.')

    def circle_diameter(self):
        print(f'The diameter of the circle is: {float(self.radius) * 2}.')

    def circle_circumference(self, pi_value=3.14159):
        print(f'The circumference of the circle is: {format(float(2 * pi_value * self.radius), "2f")}.')


class_small_circle = Circle(radius=3.2, colors='Green')
class_small_circle.circle_description()
class_small_circle.circle_area()
class_small_circle.circle_diameter()
class_small_circle.circle_circumference()
print('-' * 50)
class_big_circle = Circle(radius=4.8, colors='Blue')
class_big_circle.circle_description()
class_big_circle.circle_area()
class_big_circle.circle_diameter()
class_big_circle.circle_circumference()


# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
#
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().

class Rectangle:
    the_length: float = None
    the_breadth: float = None
    the_color: str = None

    def __init__(self, the_length, the_breadth, the_color):
        self.the_length = the_length
        self.the_color = the_color
        self.the_breadth = the_breadth

    def rectangle_description(self):
        print(f'The length is {self.the_length}, the width is {self.the_breadth} '
              f'and the color is {self.the_color}.')

    def rectangle_area(self):
        print(f'The  area of the rectangle  is: {self.the_length * self.the_breadth}.')

    def rectangle_perimeter(self):
        print(f'The perimeter of the rectangle is: {(self.the_length + self.the_breadth) * 2}. ')

    def new_color(self, color):
        self.the_color = color


class_small_rectangle = Rectangle(the_length=7, the_breadth=3, the_color='red')
class_small_rectangle.rectangle_description()
class_small_rectangle.rectangle_area()
class_small_rectangle.rectangle_perimeter()
class_small_rectangle.new_color('green')
class_small_rectangle.rectangle_description()
print('-' * 50)
class_big_rectangle = Rectangle(the_length=10, the_breadth=6, the_color='pink')
class_big_rectangle.rectangle_description()
class_big_rectangle.rectangle_area()
class_big_rectangle.rectangle_perimeter()
class_big_rectangle.new_color('yellow')
class_big_rectangle.rectangle_description()


# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

class Employee:
    surname: str = None
    first_name: str = None
    salary: float = None

    def __init__(self, surname, first_name, salary):
        self.surname = surname
        self.first_name = first_name
        self.salary = salary

    def description_of_the_emplyee(self):
        print(f'The employee surname is {self.surname}, the first name'
              f' is {self.first_name}, and his/her salary is {self.salary}$.')

    def full_name(self):
        print(f'The full name is {self.surname} {self.first_name}.')

    def monthly_salary(self):
        print(f'The monthly salary is {self.salary}$.')

    def annual_salary(self):
        print(f'The annual salary is {self.salary * 12}$.')

    def salary_raise(self, percent=float):
        print(f'The salary raise is {percent}% = {(self.salary * percent) / 100}$.')


class_employee = Employee(surname='Balanica', first_name='Nicolae', salary=4500)
class_employee.description_of_the_emplyee()
class_employee.full_name()
class_employee.monthly_salary()
class_employee.annual_salary()
class_employee.salary_raise(5.3)
print('-' * 50)
class_employee_2 = Employee(surname='Vasilescu', first_name='Ioana', salary=6250)
class_employee_2.description_of_the_emplyee()
class_employee_2.full_name()
class_employee_2.monthly_salary()
class_employee_2.annual_salary()
class_employee_2.salary_raise(4.2)


# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

class Bank_account:
    account_owner: str = None
    rib = None
    amount: float = None

    def __init__(self, account_owner, rib, amount):
        self.account_owner = account_owner
        self.rib = rib
        self.amount = amount

    def bank_account_balance(self):
        print(f'The account owner, {self.account_owner}, has in the following bank account [{self.rib}]'
              f' the amount of {self.amount} lei.')

    def account_debit(self, amount_debited=float):
        if self.amount > 0 and self.amount > amount_debited:
            self.amount = self.amount - amount_debited
            print(f'The account was debited with the amount of {amount_debited} lei.'
                  f' Your bank account balance is {format(self.amount, ".2f")} lei.')
        else:
            print('The amount you want to debit is greater than the account balance. Please try again.')

    def account_loan(self, loan_amount=float):
        self.amount = self.amount + loan_amount
        print((f'The account was borrowed with the amount of {loan_amount} lei.'
               f' Your bank account balance is {format(self.amount, ".2f")} lei.'))


class_bank_account = Bank_account(account_owner='Balanica Nicolae', rib='BT1234', amount=2539.8)
class_bank_account.bank_account_balance()
class_bank_account.account_debit(float(input('Enter the debit amount:')))
class_bank_account.account_loan(float(input('Enter the loan amount:')))
print('-' * 50)
class_bank_account = Bank_account(account_owner='Vasilescu Ioana', rib='BT2546154', amount=2539.8)
class_bank_account.bank_account_balance()
class_bank_account.account_debit(float(input('Enter the debit amount:')))
class_bank_account.account_loan(float(input('Enter the loan amount:')))


# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.

# 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
#
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon| 7 | 700 | 49000

from prettytable import PrettyTable
from datetime import datetime, date


class Invoice:
    THE_INVOICE_SERIES: str = 'RS45238INV2'
    invoice_number: int = None
    product_name: str = 'Pen'
    product_quantity: int = 1
    price_per_piece: float = 3.2

    def __init__(self, invoice_number, product_name, product_quantity, price_per_piece):
        self.invoice_number = invoice_number
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.price_per_piece = price_per_piece

    def the_name_of_the_product(self, name=str):
        self.product_name = name

    def the_quantity_of_the_product(self, quantity=int):
        self.product_quantity = quantity

    def the_price_of_the_product(self, price=float):
        self.price_per_piece = price


class_invoice = Invoice(invoice_number=1, product_name='Phone', product_quantity=7, price_per_piece=700)
class_invoice_1 = Invoice(invoice_number=0, product_name='Car', product_quantity=23, price_per_piece=100)
class_invoice_2 = Invoice(invoice_number=0, product_name='Pencil', product_quantity=12, price_per_piece=250)
t = PrettyTable([' Invoice with series: ', class_invoice.THE_INVOICE_SERIES, 'invoice Number:',
                 class_invoice.invoice_number, 'Data', date.today()])
t.add_row(['', ' ', '', '', '', ''])
t.add_row(['NR.CRT', 'Product Name', 'QUANTITY', 'PRICE/PIECE', 'TOTAL', 'Total Invoice'])
t.add_row(['-' * 20, '-' * 15, '-' * 20, '-' * 15, '-' * 15, '-' * 15])
t.add_row([1, class_invoice.product_name, class_invoice.product_quantity, class_invoice.price_per_piece,
           class_invoice.product_quantity * class_invoice.price_per_piece, ''])
t.add_row([2, class_invoice_1.product_name, class_invoice_1.product_quantity, class_invoice_1.price_per_piece,
           class_invoice_1.product_quantity * class_invoice_1.price_per_piece, ''])
t.add_row([3, class_invoice_2.product_name, class_invoice_2.product_quantity, class_invoice_2.price_per_piece,
           class_invoice_2.product_quantity * class_invoice_2.price_per_piece, ''])
t.add_row(['-' * 20, '-' * 15, '-' * 20, '-' * 15, '-' * 15, '-' * 15])
t.add_row(['', '', '', '', '', class_invoice.product_quantity * class_invoice.price_per_piece
           + class_invoice_1.product_quantity * class_invoice_1.price_per_piece
           + class_invoice_2.product_quantity * class_invoice_2.price_per_piece])

print(t)

print('*' * 121)

class_invoice = Invoice(invoice_number=2, product_name='TV', product_quantity=5, price_per_piece=900)
class_invoice_1 = Invoice(invoice_number=0, product_name='Book', product_quantity=15, price_per_piece=23.8)
class_invoice_2 = Invoice(invoice_number=0, product_name='Table', product_quantity=5, price_per_piece=158.9)
t = PrettyTable([' Invoice with series: ', class_invoice.THE_INVOICE_SERIES, 'Invoice Number:',
                 class_invoice.invoice_number, 'Data', date.today()])
t.add_row(['', ' ', '', '', '', ''])
t.add_row(['NR.CRT', 'Product Name', 'QUANTITY', 'PRICE/PIECE', 'TOTAL', 'Total Invoice'])
t.add_row(['-' * 20, '-' * 15, '-' * 20, '-' * 15, '-' * 15, '-' * 15])
t.add_row([1, class_invoice.product_name, class_invoice.product_quantity, class_invoice.price_per_piece,
           class_invoice.product_quantity * class_invoice.price_per_piece, ''])
t.add_row([2, class_invoice_1.product_name, class_invoice_1.product_quantity, class_invoice_1.price_per_piece,
           class_invoice_1.product_quantity * class_invoice_1.price_per_piece, ''])
t.add_row([3, class_invoice_2.product_name, class_invoice_2.product_quantity, class_invoice_2.price_per_piece,
           class_invoice_2.product_quantity * class_invoice_2.price_per_piece, ''])
t.add_row(['-' * 20, '-' * 15, '-' * 20, '-' * 15, '-' * 15, '-' * 15])
t.add_row(['', '', '', '', '', class_invoice.product_quantity * class_invoice.price_per_piece
           + class_invoice_1.product_quantity * class_invoice_1.price_per_piece
           + class_invoice_2.product_quantity * class_invoice_2.price_per_piece])

print(t)


# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0

class Car:
    mark: str = 'Audi'
    model: str = None
    full_speed: int = None
    current_speed: int = 0
    color: str = 'Gray'
    colors_available: set = {'Blue', 'Red', 'Yellow', 'Pink', 'Green', 'Black'}
    certified: bool = False

    def __init__(self, model, full_speed):
        self.model = model
        self.full_speed = full_speed

    def car_description(self):
        print(f'The mark is: {self.mark}.')
        print(f'The model is: {self.model}.')
        print(f'The full speed is: {self.full_speed}.')
        print(f'The current speed is: {self.current_speed}.')
        print(f'The color is: {self.color}.')
        print(f'Proof of registration: {self.certified}.')

        print('-' * 50)

    def registration(self):
        self.certified = True
        print(f'Registration: {self.certified}')

    def car_color(self, paint):
        if paint in self.colors_available:
            self.color = paint
            print(f'The new color of the car is: {self.color}.')
        assert paint in self.colors_available

    def acceleration(self, accelerate):
        self.current_speed = accelerate
        if 0 < accelerate <= self.full_speed:
            print(f'Vruuuum! The current speed is {accelerate}km/h.')
        elif accelerate > self.full_speed:
            print(f'Attention!!! The speed is {accelerate}km/h.')
            print(f'Your speed limit is {self.full_speed}km/h. ')
            print('You exceeded the speed limit. The car will stop.')

        assert accelerate > 0

    def breaking(self):
        if self.current_speed > self.full_speed:
            self.current_speed = 0
            print(f'The car stopped. The current speed is {self.current_speed} km/h.')


class_car = Car('A5', 120)
class_car.car_description()
class_car.registration()
class_car.car_color('Blue')
class_car.acceleration(5)
class_car.acceleration(90)
class_car.acceleration(100)
class_car.acceleration(121)
class_car.breaking()

print('<>' * 50)

class_car2 = Car('A8', 200)
class_car2.car_description()
class_car2.registration()
class_car2.car_color('Black')
class_car2.acceleration(80)
class_car2.acceleration(90)
class_car2.acceleration(100)
class_car2.acceleration(230)
class_car2.breaking()


# 3. Clasa TodoList
# Atribute: the_todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
#
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
# printăm detalii suplimentare.
# ○ Dacă taskul nu e în the_todo list, întrebam utilizatorul dacă vrea să-l
# adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
# dict


class Todo_List:
    the_Todo_List = {}

    def the_tasks(self):
        print('The ToDo list at the beginning of the day is:')
        self.the_Todo_List['Homework'] = 'Do your homework before 7:00 PM.'
        self.the_Todo_List['Shopping'] = 'Shoppe something to eat for today.'
        self.the_Todo_List['Cleaning'] = 'Clean the bathroom.'
        self.the_Todo_List['Sport'] = 'Go to the gym.'
        for task in self.the_Todo_List:
            print(f'{task} ')

    def tasks_completed(self, first_task):
        first_task = self.the_Todo_List.pop(first_task)
        print(f'The task "{first_task}" has been completed.')

    def show_todo_list(self):
        print('The current ToDo list is:')
        for tasks in self.the_Todo_List.keys():
            print(tasks)

    def chosen_task(self, task_name):
        if task_name in self.the_Todo_List.keys():
            print(f'You chose the task "{task_name}".')
            print(f'The details of this task are: {self.the_Todo_List.get(task_name)}.')
        elif task_name not in self.the_Todo_List.keys():
            print(f'You chose the task "{task_name}".')
            print('This task is not in your list.')
            print('Do you want to add the task to your list?')
            answer = input('Enter your answer with "yes" or "no":')
            if answer == 'yes':
                details = input('Add some details for this task:')
                self.the_Todo_List.get(task_name)
                self.the_Todo_List[task_name] = details
                print(f'Your new ToDo list is: {self.the_Todo_List}.')
            else:
                print('Good bye!')


first_list = Todo_List()
first_list.the_tasks()
first_list.tasks_completed('Cleaning')
first_list.show_todo_list()
first_list.chosen_task('Sport')
first_list.chosen_task('Sleep')
