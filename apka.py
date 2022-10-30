import sys

wiek = float(input('Podaj wiek:'))
if(wiek) >= 40:
    print("Mamy dla Ciebie specjalne ceny")
if(wiek) < 18:
    print("Serwis dostepny dla osob 18+")

if(wiek) >= 18 and (wiek)<=39:
    print("Zapraszamy")

def annoying_user(counter):
    if counter >= 5 and counter < 10:
        print("Daj spokoj, przestan wpisywac glupty xD")
    elif counter == 10:
        print("Przesadziles, nic dzis nie kupisz")
        sys.exit()

def aperol_spritz_for_free(person_sex):
    if person_sex == 'K':
        print("Dzis jest Twoj szczesliwy dzien, kobiety dostaja Aperol Spritz do kazdego zamowienia ze friko!")

def person_sex_selection():
    counter = 0
    while 1:
        person_sex = input("Podaj swoja plec. 'M' - mezczyzna, 'K' - kobieta")
        counter +=1
        if person_sex == 'K' or person_sex == 'M':
            return person_sex
        annoying_user(counter)

wiek = input("Podaj wiek: ")
# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą")
wiek = int(wiek)
if wiek >= 18:
    print("Witamy!")
    person_sex = person_sex_selection()
    aperol_spritz_for_free(person_sex)


