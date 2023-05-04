# operatii pe fisiere

# deschiderea unui fisier existent
file = open("file.txt")

# deschiderea unui fisier inexistent
# file = open("wrong_file.txt")

# afisarea continutului fisierului
print(file.read())

# afisarea continutului fisierului
# output: nu se afiseaza nimic
print(file.read())

# afisarea continutului fisierului
file.seek(0)
print(file.read())
print()

# afisarea unei liste cu liniile din fisier
file.seek(0)
print(file.readlines())
print()

# inchiderea unui fisier
file.close()

# deschiderea unui fisier dintr-o alta locatie de pe calculator cu with
with open("/Users/gojoc/CoderDojo/Files/file.txt") as file:
    content = file.read()
print(content)
print()

# deschiderea unui fisier cu permisiuni de citire
with open("file.txt", mode='r') as file:
    content = file.read()
print(content)
print()

# deschiderea unui fisier cu permisiuni de scriere pentru citire
# with open("file.txt", mode='w') as file:
#     content = file.read()

# adaugarea unui text la sfarsitul fisierului
with open("file.txt", mode='r') as file:
    print(file.read())
    print()
with open("file.txt", mode='a') as file:
    file.write("\nThis is the third line.")
with open("file.txt", mode='r') as file:
    print(file.read())
    print()

# crearea unui fisier si scrierea in el
with open("new_file.txt", mode='w') as new_file:
    new_file.write("I created this file.")
with open("new_file.txt", mode='r') as new_file:
    print(new_file.read())
    print()
with open("new_file.txt", mode='w') as new_file:
    new_file.write("This is a new file.")
with open("new_file.txt", mode='r') as new_file:
    print(new_file.read())
    print()

# exercitiu
my_file = open("my_file.txt", mode='w')
my_file.write("This is my file.")
my_file.close()
