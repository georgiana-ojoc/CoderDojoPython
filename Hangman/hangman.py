import pygame
import random

pygame.init()  # initializeaza libraria pygame

latime_ecran = 1280
inaltime_ecran = 720
ecran = pygame.display.set_mode((latime_ecran, inaltime_ecran))  # creeaza ecranul

"""
Introduceti numele jocului.
"""
pygame.display.set_caption("Hangman")  # pune titlul pe ecran
clock = pygame.time.Clock()

alb = (255, 255, 255)
negru = (0, 0, 0)
galben = (255, 235, 0)
galben_deschis = (255, 250, 125)
portocaliu = (255, 195, 75)
rosu = (200, 0, 0)
rosu_deschis = (200, 75, 75)
verde = (0, 200, 0)
verde_deschis = (75, 200, 75)
violet = (195, 125, 255)
albastru = (30, 0, 180)

imagine1 = pygame.image.load("imagine1.png")
imagine2 = pygame.image.load("imagine2.png")
imagine3 = pygame.image.load("imagine3.png")
imagine4 = pygame.image.load("imagine4.png")
imagine5 = pygame.image.load("imagine5.png")
imagine6 = pygame.image.load("imagine6.png")
imagine7 = pygame.image.load("imagine7.png")
imagini = [imagine1, imagine2, imagine3, imagine4, imagine5, imagine6, imagine7]

"""
De ce sunt 7 incercari?
"""
incercari = 7

"""
Adaugati ce cuvinte doriti pentru a fi ghicite.
"""
cuvinte = ["TERMINATOR", "TRANSFORMERS", "GODFATHER", "INCEPTION", "AVATAR", "AQUAMAN", "INTERSTELLAR", "ZOOTOPIA"]
cuvant = random.choice(cuvinte)  # alege aleatoriu un cuvant

"""
Puneti in lista "raspuns" atatea caractere '_' cate litere sunt in sirul de caractere "cuvant".
"""
raspuns = []
lungime_cuvant = len(cuvant)
for i in range(lungime_cuvant):
    raspuns.append('_')


def transforma_lista_in_sir_de_caractere_fara_spatii(lista):
    """
    Transforma lista intr-un sir de caractere si returneaza noul sir de caractere format.
    """
    sir_de_caractere = ""
    for element in lista:
        sir_de_caractere += element
    return sir_de_caractere


def transforma_lista_in_sir_de_caractere_cu_spatii(lista):
    """
    Transforma lista intr-un sir de caractere, adaugand cate un spatiu dupa fiecare caracter,
    si returneaza noul sir de caractere format.
    """
    sir_de_caractere = ""
    for element in lista:
        sir_de_caractere += element
        sir_de_caractere += ' '
    return sir_de_caractere


def afiseaza_titlu():
    """
    Introduceti numele jocului.
    """
    titlu = pygame.font.SysFont("arial", 115)  # creeaza font-ul
    obiect = titlu.render("Hangman", True, negru)  # creeaza textul titlului
    ecran.blit(obiect, (250, 150))  # afiseaza titlul


def afiseaza_dezvoltator():
    """
    Introduceti numele dezvoltatorului.
    """
    dezvoltator = pygame.font.SysFont("arial", 20)  # creeaza font-ul
    obiect = dezvoltator.render("Dezvoltat de Georgiana", True, negru)  # creeaza textul dezvoltatorului
    ecran.blit(obiect, (5, 650))  # afiseaza dezvoltatorul


def afiseaza_imagine(imagine):
    ecran.blit(imagine, (50, 50))  # afiseaza imaginea


def afiseaza_raspuns(text):
    font = pygame.font.SysFont("arial", 60)  # creeaza font-ul
    obiect = font.render(text, True, negru)  # creeaza textul raspunsului
    ecran.blit(obiect, (460, 150))  # afiseaza raspunsul


def afiseaza_text_buton(text, pozitie):
    font = pygame.font.SysFont("arial", 24)  # creeaza font-ul
    obiect = font.render(text, True, albastru)  # creeaza textul de pe buton
    ecran.blit(obiect, pozitie)  # afiseaza textul de pe buton


def afiseaza_incercari():
    font = pygame.font.SysFont("arial", 18)  # creeaza font-ul
    obiect = font.render("Incercari ramase: " + str(incercari), True, violet)  # creeaza textul incercarilor
    ecran.blit(obiect, (5, 5))  # afiseaza incercarile


def afiseaza_text_final(text):
    font = pygame.font.SysFont("arial", 120)  # creeaza font-ul
    obiect = font.render(text, True, rosu)  # creeaza textul final
    ecran.blit(obiect, (390, 150))  # afiseaza textul final


def afiseaza_raspuns_corect(text):
    font = pygame.font.SysFont("arial", 50)  # creeaza font-ul
    obiect = font.render(text, True, portocaliu)  # creeaza textul raspunsului corect
    ecran.blit(obiect, (60, 430))  # afiseaza raspunsul corect


def configureaza_buton_inceput(text, x, y, latime, inaltime, culoare_inactiv, culoare_activ):
    mouse = pygame.mouse.get_pos()  # ia pozitia mouse-ului
    click = pygame.mouse.get_pressed()  # ia click-urile
    if x < mouse[0] < x + latime and y < mouse[1] < y + inaltime:  # daca mouse-ul este pe buton
        pygame.draw.rect(ecran, culoare_activ, (x, y, latime, inaltime))  # afiseaza butonul ca activ
        if click[0] == 1:  # daca este butonul din stanga
            if text == "PLAY":
                bucla_joc()  # porneste jocul
            else:
                pygame.quit()  # iese din joc
                quit()
    else:
        pygame.draw.rect(ecran, culoare_inactiv, (x, y, latime, inaltime))  # afiseaza butonul ca inactiv
    afiseaza_text_buton(text, (x + 8, y + 8))


def configureaza_buton_litera(litera, x, y, latime, inaltime, culoare_inactiv, culoare_activ):
    mouse = pygame.mouse.get_pos()  # ia pozitia mouse-ului
    if x < mouse[0] < x + latime and y < mouse[1] < y + inaltime:  # daca mouse-ul este pe buton
        pygame.draw.rect(ecran, culoare_activ, (x, y, latime, inaltime))  # afiseaza butonul ca activ
        eveniment = pygame.event.wait()  # asteapta un eveniment
        if eveniment.type == pygame.MOUSEBUTTONDOWN and eveniment.button == 1:
            # daca butonul stang de pe mouse este apasat
            numar_de_aparitii = cuvant.count(litera)  # calculeaza de cate ori apare litera in cuvant
            if numar_de_aparitii == 0:
                pygame.draw.rect(ecran, rosu, (x, y, latime, inaltime))  # afiseaza butonul cu rosu
                global incercari
                incercari -= 1
            else:
                pygame.draw.rect(ecran, verde, (x, y, latime, inaltime))  # afiseaza butonul cu verde
                """
                Completati lista "raspuns" cu litera selectata.
                """
                for j in range(0, len(cuvant)):
                    if cuvant[j] == litera:
                        raspuns[j] = litera
                afiseaza_raspuns(transforma_lista_in_sir_de_caractere_cu_spatii(raspuns))
    else:
        pygame.draw.rect(ecran, culoare_inactiv, (x, y, latime, inaltime))  # afiseaza butonul ca inactiv
    afiseaza_text_buton(litera, (x + 8, y + 8))


def configureaza_butoane_litere():
    """
    Stiind ca:
    - liniile incep de la pozitia: (450, 450)
    - distanta intre litere pe linie este de 55
    - distanta intre litere pe coloana este de 55
    - vor fi 3 linii cu cate 9, 9 si, respectiv, 8 litere
    Completati pozitiile de mai jos pentru a afisa butoanele cu litere.
    """
    configureaza_buton_litera("A", 450, 450, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("B", 505, 450, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("C", 560, 450, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("D", 615, 450, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("E", 670, 450, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("F", 725, 450, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("G", 780, 450, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("H", 835, 450, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("I", 890, 450, 40, 40, galben, galben_deschis)

    configureaza_buton_litera("J", 450, 505, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("K", 505, 505, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("L", 560, 505, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("M", 615, 505, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("N", 670, 505, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("O", 725, 505, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("P", 780, 505, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("Q", 835, 505, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("R", 890, 505, 40, 40, galben, galben_deschis)

    configureaza_buton_litera("S", 475, 560, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("T", 530, 560, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("U", 585, 560, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("V", 640, 560, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("W", 695, 560, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("X", 750, 560, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("Y", 805, 560, 40, 40, galben, galben_deschis)
    configureaza_buton_litera("Z", 860, 560, 40, 40, galben, galben_deschis)


def incepe_joc():
    while True:
        for eveniment in pygame.event.get():
            if eveniment.type == pygame.QUIT:  # daca a fost apasat butonul X
                pygame.quit()  # iese din joc
                quit()
        ecran.fill(portocaliu)  # coloreaza ecranul
        afiseaza_titlu()
        afiseaza_dezvoltator()
        configureaza_buton_inceput("PLAY", 400, 560, 80, 40, verde, verde_deschis)
        configureaza_buton_inceput("QUIT", 800, 560, 80, 40, rosu, rosu_deschis)
        pygame.display.flip()
        clock.tick(100)


def bucla_joc():
    while True:
        for eveniment in pygame.event.get():
            if eveniment.type == pygame.QUIT:  # daca a fost apasat butonul X
                pygame.quit()  # iese din joc
                quit()
        ecran.fill(alb)  # coloreaza ecranul
        configureaza_butoane_litere()
        afiseaza_incercari()
        afiseaza_imagine(imagini[incercari - 1])
        afiseaza_raspuns(transforma_lista_in_sir_de_caractere_cu_spatii(raspuns))
        if cuvant == transforma_lista_in_sir_de_caractere_fara_spatii(raspuns):
            ecran.fill(alb)  # coloreaza ecranul
            afiseaza_text_final("AI CASTIGAT!")
            afiseaza_raspuns_corect("Raspunsul corect este: " + cuvant)
        elif incercari == 0:
            ecran.fill(alb)  # coloreaza ecranul
            afiseaza_text_final("AI PIERDUT!")
            afiseaza_raspuns_corect("Raspunsul corect era: " + cuvant)
        pygame.display.flip()
        clock.tick(100)


incepe_joc()
