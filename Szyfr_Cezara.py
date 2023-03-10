"""
Napisać program który będzie działał na zasadzie Szyfru Cezara
+Program powinien spytać użytkownika o czynność którą chce wykonać - kodowanie / odkodowanie
+Spytać o wiadomość
+Spytać o punkt przesunięcia, jeżeli uzytkownik nic nie poda to przyjmie domyślną wartość - 3
Wyświetlić zakodowany / odkodowany tekst
"""

moj_alfabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż0123456789 "

def input_uzytkownika():
    wiadomosc_uzytkownika = input("Podaj treść wiadomości: ")
    klucz = int(input("Podaj klucz: ") or 3)
    return wiadomosc_uzytkownika, klucz


def zakodowanie_wiadomosci(wiadomosc_uzytkownika, klucz):
    for element in wiadomosc_uzytkownika:
        if element in moj_alfabet:
            pozycja_w_alfabecie = moj_alfabet.find(element)
            #if pozycja w alfabecie == -1 to dodaj znak, ktory wstawil user
            pozycja_z_kluczem = (pozycja_w_alfabecie + klucz) % len(moj_alfabet)
            zakodowana_wiadomosc = moj_alfabet[pozycja_z_kluczem]
            for i in zakodowana_wiadomosc:
                print(i, end="")
                return i


def odkodowanie_wiadomosci(wiadomosc_uzytkownika, klucz):
    for element in wiadomosc_uzytkownika:
        if element in moj_alfabet:
            pozycja_w_alfabecie = moj_alfabet.find(element)
            pozycja_z_kluczem = (pozycja_w_alfabecie - klucz) % len(moj_alfabet)
            zakodowana_wiadomosc = moj_alfabet[pozycja_z_kluczem]
            for i in zakodowana_wiadomosc:
                print(i, end="")
                return i


operacja_uzytkownika = input("Chcesz zakodować czy odkodować wiadomość? Z/O ")
operacja_uzytkownika = operacja_uzytkownika.upper()

if operacja_uzytkownika == "Z":
    print("Kodujesz wiadomość")
    wiadomosc_uzytkownika, klucz = input_uzytkownika()
    zakodowanie_wiadomosci(wiadomosc_uzytkownika=wiadomosc_uzytkownika, klucz=klucz)

elif operacja_uzytkownika == "O":
    print("Odkodowujesz wiadomość")
    wiadomosc_uzytkownika, klucz = input_uzytkownika()
    odkodowanie_wiadomosci(wiadomosc_uzytkownika=wiadomosc_uzytkownika, klucz=klucz)

else:
    print("Podałeś nieprzewidzianą wartość")
    exit("Koniec działania programu")
