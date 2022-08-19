# 1.Funcție care să calculeze și să returneze suma a două numere

def the_sum_of_two_numbers(nr1, nr2):
    return nr1 + nr2


print(the_sum_of_two_numbers(4, 4))


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def number_is_odd_or_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(number_is_odd_or_even(4))


# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

def full_name(first_name, last_name, middle_name):
    return len(first_name + last_name + middle_name)


print(full_name('Balanica', 'Nicolae', 'Marian'))


# 4. Funcție care returnează aria dreptunghiului

def the_area_of_the_rectangle(lenght, width):
    return lenght * width


print(the_area_of_the_rectangle(15, 8))


# 5. Funcție care returnează aria cercului

def the_area_of_the_circle(radius, pi=3.14159):
    return float(pow(radius, 2) * pi)


print(the_area_of_the_circle(4))


# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și Talse dacă nu găsește.

def find_the_character(the_string):
    if input(f'Choose a letter:') in the_string:
        return True
    else:
        return False


print(find_the_character('Mercedes'))


# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y


def count_lower_and_upper(the_string):
    count_lower = 0
    count_upper = 0
    for i in the_string:
        if i.islower():
            count_lower += 1
        elif i.isupper():
            count_upper += 1
    print(f'The number of lower case characters is {count_lower}.')
    print(f'The number of upper case characters is {count_upper}')


count_lower_and_upper('BalaNica')


# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive

def positive_numbers_list(*the_list):
    the_list = []
    for i in range(len(the_list)):
        if the_list[i] > 0:
            the_list.append(the_list[i])
    print(the_list)


positive_numbers_list(-3, 3, -6, 8, 9, 0, 7, 7, 8)


# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

def difference_between_two_numbers(nr1, nr2):
    if nr1 > nr2:
        print(f'The first number {nr1} is greater than the second number {nr2}.')
    elif nr1 < nr2:
        print(f'The second number {nr2} is greater than the first number {nr1}.')
    else:
        print('The numbers are equal.')


difference_between_two_numbers(5, 7)
difference_between_two_numbers(-51, 6)

# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False

a_set = {3, 4, 5, 6, 7, 9}


def number_and_set(new_number, the_set):
    new_number = int(new_number)
    if new_number not in the_set:
        the_set.add(new_number)
        print('I added the new number to the set.')
        print(the_set)
        return True
    else:
        print('I did not add the number to the set. It already exists.')
        return False


print(number_and_set(4, a_set))

# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.

# 1. Funcție care primește o lună din an și returnează câte zile are acea luna

months_of_the_year = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 30
}


def days_in_a_month(the_month):
    for month, days in months_of_the_year.items():
        if the_month == month:
            return f'The month {the_month} has {days} days.'


print(days_in_a_month('March'))


# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)

def the_sum(num1, num2):
    return num1 + num2


def the_difference(num1, num2):
    return num1 - num2


def the_multiplication(num1, num2):
    return num1 * num2


def the_division(num1, num2):
    return num1 / num2


first_value = int(input('Choose the first value:'))
second_value = int(input('Choose the second value:'))
print('Options: a => sum, b => difference, c => multiplication, d => division. ')
function_selected = input('Choose what you want to know:')

if function_selected == 'a':
    print(f'The sum of {first_value} and {second_value} is {the_sum(first_value, second_value)}.')
elif function_selected == 'b':
    print(f'The difference between {first_value} and {second_value} is {the_difference(first_value, second_value)}.')
elif function_selected == 'c':
    print(f'The multiplication of {first_value} and {second_value} is {the_multiplication(first_value, second_value)}.')
elif function_selected == 'd':
    print(f'The division of {first_value} and {second_value} is {the_division(first_value, second_value)}.')
else:
    print('Please respect the request.')


# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# =>
# the_dict = {
#     0: 0,
#     1: 2,
#     2: 0,
#     3: 1,
#     4: 0,
#     5: 3,
#     6: 0,
#     7: 2,
#     8: 0,
#     9: 1
# }

def count_the_list_numbers(*elements):
    my_dict = {}
    for i in range(0, 10):
        my_dict[i] = elements.count(i)
    return my_dict


print(count_the_list_numbers(2, 2, 2, 3))


# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele

def the_maxim_value(num1, num2, num3):
    for i in range(num1, num2, num3):
        i = max(num1, num2, num3)
        return i


print(the_maxim_value(18, 25, 30))


# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)


def the_sum_of_all(element):
    x = range(0, element)
    i = sum(x, element)
    return i


print(the_sum_of_all(4))

# Exerciții Opționale - Bonus
# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
# numerele comune
#
# Exemplu:
# list1 = [1, 1, 2, 3]
#
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}

first_list = [2, 4, 6, 8, 5]
second_list = [1, 2, 3, 4, 5]


def common_numbers(elem1, elem2):
    the_result = []
    for i in first_list:
        if i in second_list:
            the_result.append(i)
    return set(the_result)


print(common_numbers(first_list, second_list))

# 2.. Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
# invalidă.

result = 0


def price_reduction(price, reduction):
    if price > 0 and reduction <= 100:
        the_result = price - (price * reduction) / 100
        return the_result
    else:
        return 'Invalid'


print(price_reduction(100, 10))

# 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)

from datetime import datetime


def date_time():
    now = datetime.now()
    print(now.strftime("Date is %d-%m-%y and time is %H:%M:%S"))


date_time()

from datetime import datetime
import pytz


def date_time_China():
    country_tyme_zone = pytz.timezone('Asia/Shanghai')
    country_time = datetime.now(country_tyme_zone)
    print(country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S"))


date_time_China()

# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
# Crăciun dacă nu vrei să ne zici cand e ziua ta :)


import datetime


def get_user_birthday():
    year = int(input('Enter the year of your birth: '))
    month = int(input('Enter the month of your birth: '))
    day = int(input('enter the day of your birth: '))
    birthday = datetime.datetime(year, month, day)
    return birthday


def calculate_dates(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year + 1, original_date.month, original_date.day)
    delta = date2 - date1
    days = delta.total_seconds() / 60 / 60 / 24
    return days


bd = get_user_birthday()
now_ = datetime.datetime.now()
c = calculate_dates(bd, now_)
print(c.__int__())
