
# Exerciții obligatorii - grad de dificultate: Usor spre Mediu
# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.
#
# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# ● Afișeaz-o
# ● Inversează ordinea folosind slicing și suprascrie această listă.
# ● Printează varianta actuală (inversată).
# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.
# Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
# suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
# suprascrierea automat și permanentizează aceste modificări. Ambele variante
# își găsesc utilitatea în funcție de ce ne dorim în acel moment.
#
musical_notes = ['DO', 'RE', 'MI', 'FA', 'SO', 'LA', 'SI', 'DO']
print(musical_notes)
musical_notes = musical_notes[::-1]
print(musical_notes)
musical_notes.reverse()
print(musical_notes)



# 2. De câte ori apare ‘do’?

musical_notes = ['DO', 'RE', 'MI', 'FA', 'SO', 'LA', 'SI', 'DO']
print(musical_notes.count('DO'))

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.

first_list = [3, 1, 0, 2]
second_list = [6, 5, 4]
new_list = first_list + second_list # first version
print(new_list)
first_list.extend(second_list) # second version
print(first_list)

# 4.
# ● Sortează și afișază lista generată la exercițiul anterior.
# ● Sortează numărul 0 folosind o funcție.
# ● Afișaza iar lista.

first_list = [3, 1, 0, 2]
second_list = [6, 5, 4]
new_list = first_list + second_list
print(new_list)
new_list.sort()
print(new_list)
new_list.pop(0)
print(new_list)

# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
# ● Lista este goală.
# ● Lista nu este goală.

first_list = [3, 1, 0, 2]
second_list = [6, 5, 4]
new_list = first_list + second_list
print(new_list)
new_list.sort()
print(new_list)
if new_list == 0:
    print('The list is empty.')
else:
    print('The list is not empty.')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.

first_list = [3, 1, 0, 2]
second_list = [6, 5, 4]
new_list = first_list + second_list
print(new_list)
new_list.clear() # stergem continutul listei
print(new_list)
del new_list # mai exista si varianta aceasta unde o stergem de tot
# daca vom da un print la acest statement ne va da o eroare pentru ca lista nu mai exista

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
#
first_list = [3, 1, 0, 2]
second_list = [6, 5, 4]
new_list = first_list + second_list
print(new_list)
new_list.clear()
print(new_list)
if len(new_list) == 0:
    print('The list is empty.')
else:
    print('The list is not empty')


# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
x = dict1.keys()
print(x)

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(f' Ana a luat nota {dict1["Ana"]}.')
print(f' Gigel a luat nota {dict1["Gigel"]}.')
print(f' Dorel a luat nota {dict1["Dorel"]}.')

# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1)
dict1['Dorel'] = 6
print(dict1)

# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 6}
dict1.pop('Gigel')
print(dict1)
dict1.update({'Ionica': 9}) #version one
print(dict1)
dict1['Ionica'] = 9# version two
print(dict1)

# 12.
# Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
# ● Afișeaza zile_sapt
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
# nu poti duplica o valoare intr-un set (in cazul unui add,nu va afisa nimic diferit)
zile_sapt.add('luni')
print(zile_sapt)
# luni poate fi adagat cu majuscule ('Luni)

# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămânii.')
else:
    print('Weekend nu este un subset al zilelor din săptămânii.')

# 14. Afișează diferențele dintre aceste 2 seturi.

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
print(zile_sapt.difference(weekend))

#  15. Afișază intersecția elementelor din aceste 2 seturi.

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
print(zile_sapt.intersection(weekend))

# Exerciții Opționale - grad de dificultate: Mediu spre greu(may need google) .
# 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișaza a intra x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# - Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
# teren’
# - Afișază ‘mai ai z schimbări’
# Testează codul cu diferite valori

team = ['Hagi', 'Mutu', 'Chivu', 'Munteanu', 'Radoi']
changes_made = 0
maximum_changes_allowed = 3

print(f'The starting team is {team}.')
while maximum_changes_allowed > changes_made:
    get_out = input('Choose the player who comes out:')
    get_in = input('Choose the player who comes in:')
    if get_in not in team:
        if len(get_in) != 0:
            if get_out in team:
                maximum_changes_allowed = maximum_changes_allowed - 1
                team.remove(get_out)
                team.append(get_in)
                print(f'The current team is {team}.')
                if changes_made == maximum_changes_allowed:
                    print('You have no more changes.')
                else:
                    print(f'You have  {maximum_changes_allowed} more changes.')
                    print('-' * 50)
            else:
                print(f'The change cannot be made because the player "{get_out}" is not on the field.')
                print(f'The current team is {team}.')
                print(f'You have {maximum_changes_allowed} more changes.')
        else:
            print('You have not entered anything. Please try again.')
    else:
        print('The player is already on the field. Please try again.')
        print(f'The current team is {team}.')
