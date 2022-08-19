# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.

cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
        'Fiat', 'Trabant', 'Opel']
for car in range(len(cars)):
    print(f'My favorite car is {cars[car]}.')  # for
print('-' * 50)
for car in cars:
    print(f'My favorite car is {car}.')  # for each
print('-' * 50)
car = 0
while car < len(cars):
    print(f'My favorite car is {cars[car]}.')  # while
    car += 1

# 2. Aceeași listă:
# Folosește un for else
# În for
#
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.

cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
        'Fiat', 'Trabant', 'Opel']

for car in range(1, len(cars) - 1):
    cars[car] = cars[car].upper()
else:
    print(cars)

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
        'Fiat', 'Trabant', 'Opel']
for car in range(len(cars)):
    if cars[car] == 'Mercedes':
        break
    print(f'We found the car {cars[car]} , we still looking.')
print('We found your car.')

# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.

cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
        'Fiat', 'Trabant', 'Opel']
for car in cars:
    if car == 'Lăstun' or car == 'Trabant':
        continue
    print(f'You might like the car {car}.')

# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
#
# ● Printează Modele vechi: x.
# ● Modele noi: x.

cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
        'Fiat', 'Trabant', 'Opel']
old_cars = []
for car in list(cars):
    if car == 'Lăstun' or car == 'Trabant':
        cars.remove(car)
        cars.append('Tesla')
        old_cars.append(car)
print(f'Old cars : {old_cars}')
print(f'New cars : {cars}')

# 6. Având dict:
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.

pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
for car, price in pret_masini.items():
    if price <= 15000:
        print(car)
print('-' * 50)

for car, price in pret_masini.items():
    if price <= 15000:
        print(car, '-', price, 'euro')

print('-' * 50)

for car, price in pret_masini.items():
    if price < 15000:
        print(f'For a budget below 15,000 euros, you can choose the car {car}.')

# 7. Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).


numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
count = 0
for i in numbers:
    if i == 3:
        count += 1
print(f'The number 3 appears {count} times.')

# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
the_sum = 0
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for number in numbers:
    the_sum = the_sum + number
print(f'The sum of the numbers is {the_sum}.')

# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).

numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max_number = 0
for i in range(len(numbers)):
    if numbers[i] > max_number:
        max_number = numbers[i]
print(f'The largest number is {max_number}.')

print('-' * 50)

for number in numbers:
    if number > max_number:
        max_number = number
print(f'The largest number is {max_number}.')

# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.

numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for number in range(len(numbers)):
    if numbers[number] > 0:
        numbers[number] = numbers[number] * -1
print(numbers)

# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need
# Google.

# 1.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișeaza cele 4 liste la final

other_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
even_numbers = []
odd_numbers = []
positive_numbers = []
negative_numbers = []
for n in range(len(other_numbers)):
    if other_numbers[n] % 2 == 0:
        even_numbers.append(other_numbers[n])
    elif other_numbers[n] % 2 != 0:
        odd_numbers.append(other_numbers[n])
    if other_numbers[n] > 0:
        positive_numbers.append(other_numbers[n])
    elif other_numbers[n] < 0:
        negative_numbers.append(other_numbers[n])
print(even_numbers)
print(odd_numbers)
print(positive_numbers)
print(negative_numbers)
# functioneaza la fel si cu for each

# 2. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.

other_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
good_order = []
minim = 0

while other_numbers:
    minim = other_numbers[0]
    for n in other_numbers:
        if n < minim:
            minim = n
    good_order.append(minim)
    other_numbers.remove(minim)
print(good_order)

# 3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
#
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!

import random

secret_number = random.randint(1, 30)
number_guessed = 0
while number_guessed != secret_number:
    number_guessed = int(input('Choose a number between 1 and 30:'))
    if number_guessed < secret_number:
        print('The secret number is higher. Please try again.')
    if number_guessed > secret_number:
        print('The secret number is lower. Please try again.')
    if number_guessed == secret_number:
        break
print('Congratulations! You guessed it!')

# 4. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
#
# Ex:3
# 1
# 22
# 333

number = int(input('Choose a number:'))
for n in range(number + 1):
    for j in range(n):
        print(n, end='')
    print('')

# 5.
# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’

tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for i in tastatura_telefon:
    for j in i:
        print(f'The current number is {j}.')

# Exercitii extra:
# Intr-o lista goala sa adaugam sirul de fibonacci pana la 1000 si sa printam lista

x = 0
y = 1
n = int(input("Enter the number of terms: "))
i = 2
fibo_list = [x, y]
while i < n:
    fibo_numbers = x + y
    fibo_list.append(fibo_numbers)
    x = y
    y = fibo_numbers
    i += 1
print(fibo_list)
