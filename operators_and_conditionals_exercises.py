# Exerciții obligatorii - grad de dificultate: Ușor spre Mediu

'''1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
else.'''

# un if else te ajuta sa controlezi pe unde sa curga codul.


# 2. Verifică și afișează dacă x este număr natural sau nu.

x = int(input('Insert a number:'))
if x > 0:
    print(f'{x} is a natural number.')
else:
    print(f'{x} is not a natural number.')



# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.

x = int(input('Insert a number:'))
if x < 0:
    print(f'{x} is a negative number.')
elif x > 0:
    print(f'{x} is a positive number.')
else:
    print(f'{x} is a neutral number.')



# 4. Verifică și afișează dacă x este între -2 și 13.

x = int(input('Insert a number:'))
if x in range(-2, 13):
    print('True')
else:
    print('False')



# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.

x = int(input('Insert a number x:'))
y = int(input('Insert a number y:'))
dif = (x - y)
print(f'The difference between x and y is {dif}.')
if dif < 5:
    print('True')
else:
    print('False')



# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.

x = int(input('Insert a number:'))
if x not in range(5, 27):
    print('True')
else:
    print('False')



# 7. x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
# mare.

x = int(input('Insert a number x:'))
y = int(input('Insert a number y:'))
if x > y:
    print(f'{x} is bigger than {y}')
elif y > x:
    print(f'{y} is bigger than {x}.')
else:
    print('The numbers are equal.')



# 8. X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

x = int(input('Insert a number x:'))
y = int(input('Insert a number y:'))
z = int(input('Insert a number y:'))

if x == y == z:
    print('The triangle is equilateral')
elif x == y or z == y or z == x:
    print('The triangle is isosceles. ')
else:
    print('The triangle is scalene. ')



# 9. Citește o literă de la tastatură.
# Verifică și afișează dacă este vocală sau nu

vowels = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')
letter = input('Choose a letter:')
if letter in vowels:
    print(f'"{letter}" is a vowel.')
else:
    print(f'"{letter}" is a consonant.')



# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

grade = int(input('Insert your grade:'))
if 4 < grade < 7:  # notele 5 si 6 se incadreaza la calificativul 'E'
    print('Congrats, your grade is "E". You passed the exam.')
elif 6 < grade < 8:
    # se poate scrie si direct 7 insa in cazul unui float nu trebuie sa modific tot codul
    print('Congrats, your grade is "D". You passed the exam.')
elif 7 < grade < 9:  # idem cu 8
    print('Congrats, your grade is "C". You passed the exam.')
elif 8 < grade < 10:  # idem cu 9
    print('Congrats, your grade is "B". You passed the exam.')
elif grade > 9:  # idem cu 10
    print('Congrats, your grade is "A". You passed the exam. You are the best.')
else:
    print('Sorry, your grade is "F". You failed the exam.')



# Exerciții Opționale - grad de dificultate: Mediu spre greu - might need Google.

# 1.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

x = int(input('Insert a number with minimum four digits:'))
x = str(x)
if len(x) >= 4:
    print(f'The number {x} is True.')
else:
    print(f'The number {x} has les than four digits. Please try again.')



# 2.Verifică dacă x are exact 6 cifre.
x = int(input('Insert a six digits number:'))
x = str(x)
if len(x) == 6:
    print('Your number is correct.')
else:
    print('Your number is wrong.')



# 3.Verifică dacă x este număr par sau impar (x e int).

x = int(input('Enter a number:'))
if x % 2 == 0:
    print('Your number is even.')

else:
    print('Your number is odd.')



# 4. x, y, z (int)
# Afișează care este cel mai mare dintre ele?

x = int(input('Enter the number X:'))
y = int(input('Enter the number Y:'))
z = int(input('Enter the number Z:'))

if x == y != z or y == z != x or z == x != y:
    print('Wrong combination.Choose another option.')
elif x > y and x > z:
    print('X is the largest number.')
elif y > x and y > z:
    print('Y is the largest number.')
elif z > x and z > y:
    print('Z is the largest number.')
else:
    print('All numbers are equal.')



# X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.

x = int(input('Enter the value of x :'))
y = int(input('Enter the value of Y:'))
z = int(input('Enter the value of Z:'))

if x ** 2 + y ** 2 == z ** 2:
    print('The triangle is right-angled.')
elif y ** 2 + z ** 2 == x ** 2:
    print('The triangle is right-angled.')
elif z ** 2 + x ** 2 == y ** 2:
    print('The triangle is right-angled.')
else:
    print('The triangle is not right-angled')


# 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citiți de la tastatură un int x
# ● Afișează stringul fără ultimele x caractere
# Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte

string = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Alegeti un numar intre 0 si 57:'))
print(f'"{string[:-x]}"')



# 7.Același string. Declară un string nou care să fie format din primele 5 caractere
# + ultimele 5

string = 'Coral is either the stupidest animal or the smartest rock'
string_nou = string[:5] + string[-5:]
print(string_nou)



# 8. Același string.
# ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
# este o funcție care te ajuta sa faci asta)
# ● Folosind această variabilă + slicing, afișează tot stringul până la acest
# cuvant
# ● output: 'Coral is either the stupidest animal or the smartest

string = 'Coral is either the stupidest animal or the smartest rock'
index = string.index('rock')
print(index)
print(f'"{string[:index]}"')



# 9. Citește de la tastatura un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat

string = input('Enter a  string:')
assert string[0].lower() == string[-1].lower()



# 10. Avand stringul '0123456789'
# ● Afișați doar numerele pare
# ● Afișați doar numerele impare
# (hint: folositi slicing, controlați din pas)

string = '0123456789'
print(string[1::2])
print(string[2::2])



# #Exerciții Bonus (may need google) .

# 11. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Luați un numărul ghicit de la utilizator
# Verificați și afișați dacă utilizatorul a ghicit
# Veți avea 3 opțiuni
# ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# ● Ai ghicit. Felicitari! Ai ales x si zarul a fost y

import random

user1 = random.randint(1, 6)
user2 = int(input('Dati cu zarul si introduceti numarul de pe zar:'))
if user2 < user1:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {user2} dar a fost {user1}.')
elif user2 > user1:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {user2} dar a fost {user1}.')
else:
    print(f'Ai ghicit. Felicitari! Ai ales {user2} si zarul a fost {user1}.')
