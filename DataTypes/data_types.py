# tipul de date numeric
print("Tipul de date numeric")

my_age = 13 // 5
print(my_age)

my_age = 10.0 / 2
print(my_age)

print()

# tipul de date string (sir de caractere)
print("Tipul de date string (sir de caractere)")

my_string = "Ana Maria"
print(my_string[4])
print(my_string[4:])
print(my_string[1:4])
print(my_string[::-1])

# my_string[0] = 'a'

print()

# liste
print("Liste")

my_list = [420, "sambata", '*']
print(my_list)

my_list.append(2.5)
print(my_list)

value = my_list.pop()
print(value)
print(my_list)

my_list = [8, 20, 5, -1, 16]
my_list.sort()
print(my_list)
print(my_list[-1])

print()

# dictionare
print("Dictionare")

my_dictionary = {"cheie": "valoare", "k2": 5, "k3": [1, 2, 3]}
print(my_dictionary["cheie"])
print(my_dictionary["k3"])
print(my_dictionary["k3"][0])

my_dictionary = {"k1": 'x'}
my_dictionary["k1"] = 1
my_dictionary["k2"] = 'x'
print(my_dictionary)

my_dictionary = {"culoare": "verde", "clasa": 10}
print(my_dictionary)

my_dictionary = {"specie": "caine"}
my_dictionary["nume_catel"] = "Alfie"
print(my_dictionary)

print()

# tupluri
print("Tupluri")

my_tuple = (1, 2, 3)
# my_tuple[0] = 5
print(my_tuple)
print(my_tuple[0])

print()

# seturi
print("Seturi")

my_set = {1, 2, 3, 4, 4, "text"}
print(my_set)

# print(my_set[0])
# my_set[0] = 5

my_set = {1}
my_set.add(2)
my_set.add(2)
print(my_set)

my_set = {1}
my_set.update([1, 2, 3, 4])
print(my_set)

my_set = {2, 3}
my_set.update([4, "text"], {1, 2, 6, 8})
print(my_set)

value = my_set.pop()
print(value)
print(my_set)

my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)

my_set.discard(2)
print(my_set)

my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)

# my_set.remove(2)

"""
1. Ce tip de dată este următoarea structură: {"culoare": "verde", "numar": 13.5}?
a. tuplu
b. dicționar (corect)
c. listă
d. set

2. Într-un set pot exista două elemente cu aceeași valoare?
a. adevărat
b. fals (corect)

3. Ce se afișează în urma rulării următoarelor linii de cod?
values = (1, "verde", 2)
values.append(3.5)
print(values)
a. (1, "verde", 2, 3.5)
b. "values"
c. [1, "verde", 2, 3.5]
d. eroare, deoarece tuplele nu pot fi modificate (corect)

4. Având tuplul: tuplu = ('a', 'b', 'c'), ce valoare returnează tuplu[1]?
a. 'a'
b. 'b' (corect)
c. 'c'
d. eroare

5. Ce tip de dată este următoarea structură: [2022, 2023, 2024]?
a. tuplu
b. dicționar
c. listă (corect)
d. set

6. Ce se afișează în urma rulării următoarelor linii de cod?
values = {10, 20, 30, 20, 40}
print(values)
a. {10, 20, 30, 20, 40}
b. {10, 20, 40}
c. {10, 20, 30, 40} (corect)
d. {10, 20, 20, 30, 40}

7. Având setul: my_set = {"dog", "cat", "parrot"}, ce valoare returnează my_set[1]?
a. 'a'
b. 'b'
c. 'c'
d. eroare (corect)

8. Ce se afișează în urma rulării următoarelor linii de cod?
values = {10, 20, 30}
values.discard(20)
print(values)
a. {10, 30} (corect)
b. eroare
c. 20
d. {10, 20, 30}

9. Ce se afișează în urma rulării următoarelor linii de cod?
values = {10, 20, 30}
values.update([20, 5, 30])
print(values)
a. eroare
b. [10, 20, 5, 30]
c. {10, 20, 30, 20, 5, 30}
d. {10, 20, 5, 30} (corect)

10. Având tuplul: my_tuple = (1, 4, 'c'), ce valoare returnează len(my_tuple)?
a. 1
b. 3 (corect)
c. eroare
d. 4
"""
