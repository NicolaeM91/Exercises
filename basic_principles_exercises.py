#Tema 1 _ Setup, Variabile, Tipuri de date
#Exerciții obligatorii - grad de dificultate: Ușor spre Mediu:

# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

 # O variabila este un container din memorie care stocheaza valori.


# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
# variabilă :

# - string
# - int
# - float
# - bool
#
# Observație: Valorile vor fi alese de tine după preferințe.

string = 'casa'
int = 9
float = 3.4
bool = True

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.

print(type(string))
print(type(int))
print(type(float))
print(type(bool))

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
# aceeași variabilă (suprascriere):
# - Verifică tipul acesteia.

float = round(float)
print(float)
print(type(float))

# 5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
#
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.

print(f'Bunicii mei au o {string} foarte veche.')
print(f'Matusa mea are {int} pisici.')
print(f'Am cumparat {float} kg de cartofi.')
print(f'Este {bool} tot ce am citit in ziar.')

# 6. Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.

nume = input('Alege un nume: ')
prenume = input('Alege un prenume:')
nume_complet = len(nume + prenume)
print(f'Numele complet are {nume_complet} caractere.')


# 7. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
#
# - afișează de câte ori apare cuvântul 'the';

string2 = 'Coral is either the stupidest animal or the smartest rock'
print(f'Cuvantul "the" apare de {string2.count("the")} ori.')

# 8. Același string.
# ● Afișează de câte ori apare cuvântul 'the';
# ● Printează rezultatul.

string2 = 'Coral is either the stupidest animal or the smartest rock'
print(f'Cuvantul " the " apare de {string2.count(" the ")} ori.')

# 9. Același string.
# ● Folosiți un assert ca să verificați dacă acest string conține doar numere.

string2 = 'Coral is either the stupidest animal or the smartest rock'
assert string2.isnumeric()
print('da')


# Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai
# nevoie de Google).

# 1. Exercițiu:
# - citește de la tastatură un string de dimensiune impară;
# - afișează caracterul din mijloc.

string_impar = 'ambalaj'
print(string_impar[len(string_impar)//2])

# 2. Folosind assert, verifică dacă un string este palindrom.

cuvant = 'racecar'
assert cuvant == cuvant[::-1]
print('Cuvantul este palindrom.')

# 3. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.

string = 'alabala portocala'
a, b = string.split()
print(a)
print(b)

# 4. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.

string = input('Introduceti stringul:')
first_char = string[0]
last_char = string[-1]
string_nou = first_char + string[1:-1].replace(first_char, first_char.upper()) + last_char
print(string_nou)

string2 = input('Introduceti un alt string:')
first_char2 = string2[0]
last_char2 = string2[-1]
string_nou2 = first_char2 + string2[1:-1].replace(first_char2, first_char2.upper()) + last_char2
print(string_nou2)

# 5.Exercițiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ****

user = input('Alegeti un user:')
parola = input('Alegeti o parola:')
print(f'Parola pentru userul {user} este {len(parola) * "*"} si are {len(parola)} caractere.')


