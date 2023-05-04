# WHILE

# exemplul 1: bucla infinita
# i = 1
# while i < 6:
#     print(i)
#
# print()

# exemplul 2: 1 2 3 4 5
i = 1
while i < 6:
    print(i)
    i += 1

print()

# exemplul 3: 3 6 9
i = 3
while i < 10:
    print(i)
    i += 3

print()

# exemplul 4: 6 9 12
i = 3
while i < 10:
    i += 3
    print(i)

print()

# exemplul 5: 1 2 3 4 5 6 7 8 9 10 11 12 13 - 13
i = 1
while i <= 13:
    print(i)
    i += 1
else:
    print("i este mai mare decat 13")

print()

# exercitiul 1
i = 4
while i < 57:
    print(i)
    i += 2

print()

# exercitiul 2: 0 3 6 9 12 15 18
i = 0
while i < 21:
    print(i)
    i += 3

print()

# exercitiul 3: bucla infinita
# i = 63
# while i > 14:
#     print(i)
#     i += 2
#
# print()

# exercitiul 4: 55
i = 1
n = 10
suma = 0
while i <= n:
    suma = suma + i
    i = i + 1
print("Suma este: ", suma)

print()

x = 0
while x < 5:
    print(f"Valoarea curenta a lui x este: {x}")
    x += 1
else:
    print(f"x nu este mai mic decat 5")

print()

# exercitiul 5: C e o
my_string = "CoderDojo"
i = 0
while i < len(my_string):
    if i % 3 == 0:
        print(my_string[i])
    i += 1

print()

# exercitiul 6: o infinitate
# i = 2
# while i < 10:
#     print(i)
#     i -= 2
#
# print()

# exercitiul 7: Today is Sturdy.
my_string = "Today is Saturday."
new_string = ""
i = 0
while i < len(my_string):
    if my_string[i] != 'a':
        new_string += my_string[i]
    i += 1
print(new_string)

print()

# METODE

# sir de caractere
my_string = "Acesta este un text."
print(my_string.upper())
print(my_string.lower())
print(my_string.split())
print(my_string.isdigit())

print()

# lista
my_list = [2, 1, 3]
print(my_list.pop())
my_list.append(4)
my_list.sort()
my_list.reverse()
print(my_list)

print()

# set
my_set = {"rosu", "verde", "albastru"}
my_set.add("galben")
my_set.update(["galben"])
print(my_set)
print(my_set.intersection(["rosu", "albastru"]))

print()

# dictionar
my_dictionary = {"5A": 23, "7B": 28}
print(list(my_dictionary.keys()))
print(list(my_dictionary.values()))
print(my_dictionary.pop("5A"))
print(my_dictionary)

print()
