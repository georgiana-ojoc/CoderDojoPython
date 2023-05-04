# FUNCTII
import datetime


# exemplul 1
def afiseaza_mesaj():
    print("Noi suntem la CoderDojo.")


afiseaza_mesaj()
print()


# exemplul 2
def afiseaza_salut(nume):
    print(f"Hello, {nume}!")


afiseaza_salut("Elena")
print()


# exemplul 3
def aduna_numar_la_lista(lista, numar):
    j = 0
    while j < len(lista):
        lista[j] += numar
        j += 1
    print(lista)


aduna_numar_la_lista([1, 2, 3], 10)
print()


# exemplul 4
def calculeaza_suma(a, b):
    return a + b


print(calculeaza_suma(10, 20))
print()


# exemplul 5
def concateneaza_siruri(a, b):
    c = a + b
    return c.upper()


sir = concateneaza_siruri("alfa", "bet")
print(sir)
print()


# exemplul 6
def este_divizibil_cu_5(y):
    if y % 5 == 0:
        return True
    else:
        return False


print(este_divizibil_cu_5(13))
print()


# exercitiul 1
def maxim(a, b):
    if a > b:
        return a
    else:
        return b


print(maxim(10, 20))
print()


# exercitiul 2
def aduna(lista):
    return sum(lista)


print(aduna([1, 3, 5, 7]))
print()


# exercitiul 3
def inlocuieste_litera_o(text):
    text_nou = ""
    for caracter in text:
        if caracter == 'o':
            text_nou += '*'
        else:
            text_nou += caracter
    return text_nou


print(inlocuieste_litera_o("Am venit la CoderDojo."))
print()


# exercitiul 4
def numere_impare(lista):
    impare = []
    for numar in lista:
        if numar % 2 == 1:
            impare.append(numar)
    return impare


print(numere_impare([1, 2, 3, 4, 5]))
print()

# exercitiul 5
"""
Scrieți o funcție care primește ca parametri două liste și returnează numărul care se regăsește numai într-una dintre
liste. Cele două liste conțin aceleași numere, însă una dintre ele conține unul în plus.
"""


def numar_in_plus(lista_1, lista_2):
    set_1 = set(lista_1)
    set_2 = set(lista_2)
    if len(set_1) > len(set_2):
        diferenta = set_1.difference(set_2)
    else:
        diferenta = set_2.difference(set_1)
    return diferenta.pop()


print(numar_in_plus([1, 4, 5, 7, 9], [1, 5, 7, 9]))
print()

# exercitiul 6
"""
Scrieți o funcție care primește ca parametru o listă de dicționare cu numele și rasa unor câini și returnează o listă de
dicționare cu numele, rasa și vârsta acelor câini.
"""


def lista_de_caini(lista):
    lista_noua = []
    for dictionar in lista:
        dictionar_nou = dictionar.copy()
        dictionar_nou["vârstă"] = 5
        lista_noua += [dictionar_nou]
    return lista_noua


print(lista_de_caini([{"nume": "Grivei", "rasa": "Golden Retriever"}, {"nume": "Rina", "rasa": "Shiba Inu"}]))
print()

# exercitiul 7
"""
Scrieți un program care afișează toți divizorii unui număr natural.
"""


def divizori(numar):
    lista = [1]
    for divizor in range(2, numar // 2 + 1):
        if numar % divizor == 0:
            lista += [divizor]
    lista += [numar]
    return lista


print(divizori(63))
print()

# exercitiul 8
"""
Scrieți un program care afișează oglinditul fiecărui număr natural dintr-o listă.
"""


def oglindit(numar):
    # return int(str(numar)[::-1])
    numar_nou = 0
    while numar > 0:
        numar_nou *= 10
        numar_nou += numar % 10
        numar //= 10
    return numar_nou


def lista_de_oglindite(lista):
    # return [oglindit(numar) for numar in lista]
    lista_noua = []
    for numar in lista:
        lista_noua += [oglindit(numar)]
    return lista_noua


print(lista_de_oglindite([123, 546, 223]))
print()

# exercitiul 9
"""
Scrieți o funcție care primește ca parametru o listă de nume și returnează o listă cu șiruri de caractere sub forma
„Salut, {nume}!”.
"""


def lista_de_saluturi(lista):
    lista_noua = []
    for nume in lista:
        lista_noua.append(f"Salut, {nume}!")
    return lista_noua


print(lista_de_saluturi(["Ana", "Matei"]))
print()

# exercitiul 10
"""
Scrieți o funcție care primește ca parametru o listă de numere și returnează un tuplu de forma (bool, list), astfel: 
dacă lista primită este ordonată, va returna True și lista nemodificată, iar dacă lista nu este ordonată, va returna 
False și lista ordonată.
"""


def lista_sortata(lista):
    lista_noua = sorted(lista)
    if lista == lista_noua:
        return True, lista
    return False, lista_noua


print(lista_sortata([-5, -10, 2]))
print(lista_sortata([1, 2, 3]))
print()

# exercitiul 11
"""
Scrieți o funcție care primește ca parametru un număr natural n și returnează al n-lea număr din șirul lui Fibonacci.
"""


def fibonacci(n):
    if n < 3:
        return 1
    numar_1 = 1
    numar_2 = 1
    while n > 2:
        numar_3 = numar_1 + numar_2
        numar_1, numar_2 = numar_2, numar_3
        n -= 1
    return numar_2


print(fibonacci(2))
print(fibonacci(10))
print()

# exercitiul 12
"""
O literă poate exprima mai multe sunete (x), iar un sunet poate fi scris cu mai multe litere (ce, ci, chi, che,
ge, gi, ghe, ghi). Scrieți o funcție care returnează True dacă numărul de sunete este egal cu numărul de litere și
False altfel, pentru un cuvânt primit ca parametru.
"""


def litere_egal_sunete(cuvant):
    lista = ['x', 'ce', 'ci', 'chi', 'che', 'ge', 'gi', 'ghe', 'ghi']
    for element in lista:
        if element in cuvant:
            return False
    return True


print(litere_egal_sunete("carte"))
print(litere_egal_sunete("examen"))
print(litere_egal_sunete("Gheorghe"))
print()

# exercitiul 13
"""
Scrieți o funcție care primește ca parametru un număr ce reprezintă anul nașterii al unei persoane și returnează
generația din care face parte persoana respectivă.
"""

"""
Gen Alpha: 0-12 ani ​

Gen Z: 13-25 ani​

Gen Y: 26-41 ani​

Gen X: 42-57 ani​

Boomers: 58 – 76 ani​

Silent Gen: 76-94 ani
"""


def generatie(an):
    varsta = datetime.date.today().year - an
    if varsta <= 0:
        return None
    if 0 <= varsta <= 12:
        return "Alpha"
    if varsta <= 25:
        return 'Z'
    if varsta <= 41:
        return 'Y'
    if varsta <= 57:
        return 'X'
    if varsta <= 76:
        return "Boomers"
    if varsta <= 94:
        return "Silent"


print(generatie(1999))
print(generatie(1968))
print()

# exercitiul 14
"""
Scrieți o funcție care primește ca parametri două liste a câte șase numere și returnează un tuplu format dintr-un
boolean și o listă, astfel: dacă patru sau mai multe dintre numerele din liste sunt comune, se returnează
(True, listă_numere_comune), altfel se returnează (False, lista_numere_comune).
"""


def intersectie(lista_1, lista_2):
    lista = []
    for numar in lista_1:
        if numar in lista_2:
            lista_2.remove(numar)
            lista += [numar]
    return lista


def numere_comune(lista_1, lista_2):
    lista = intersectie(lista_1, lista_2)
    # return ((False, lista), (True, lista))[len(lista) >= 4]
    return (True, lista) if len(lista) >= 4 else (False, lista)


print(numere_comune([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 7]))
print(numere_comune([24, 21, 1, 35, 21, 49], [21, 35, 50, 2, 49, 1]))
print(numere_comune([12, 43, 55, 3, 21, 66], [17, 29, 35, 3, 55, 4]))
