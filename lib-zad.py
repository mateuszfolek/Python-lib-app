stale_id = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
ksiazki = {}
studenci = set()
wypozyczone = {}

def dodaj_ksiazke():
    print("------------------------")
    id_ksiazki = int(input("Podaj ID książki: "))
    if id_ksiazki in stale_id:
        if id_ksiazki not in ksiazki:
            tytul = input("Podaj tytuł książki: ")
            ksiazki[id_ksiazki] = tytul
            print("Książka dodana pomyślnie.")
        else:
            print("Książka o tym ID już istnieje.")
    else:
        print("Nieprawidłowe ID książki.")
    print("------------------------")

def dodaj_studenta():
    print("------------------------")
    student = input("Podaj imię studenta: ")
    if student not in studenci:
        studenci.add(student)
        print("Student dodany pomyślnie.")
    else:
        print("Student już istnieje.")
    print("------------------------")

def wypozycz_ksiazke():
    print("------------------------")
    id_ksiazki = int(input("Podaj ID książki do wypożyczenia: "))
    if id_ksiazki in ksiazki:
        if id_ksiazki not in wypozyczone:
            student = input("Podaj imię studenta: ")
            if student in studenci:
                wypozyczone[id_ksiazki] = student
                print("Książka wypożyczona pomyślnie.")
            else:
                print("Brak studenta - załóż kartę biblioteczną.")
        else:
            print("Książka jest już wypożyczona.")
    else:
        print("Brak książki o tym ID.")
    print("------------------------")

def liczba_ksiazek():
    print("------------------------")
    print("Liczba książek:", len(ksiazki))
    print("------------------------")
    print("Lista książek:")
    for id_ksiazki, tytul in ksiazki.items():
        print(f"ID: {id_ksiazki}, Tytuł: {tytul}")
    print("------------------------")

def liczba_wypozyczonych():
    print("------------------------")
    print("Liczba wypożyczonych:", len(wypozyczone))
    if wypozyczone:
        print("------------------------")
        print("Lista wypożyczonych książek:")
        for id_ksiazki, student in wypozyczone.items():
            print(f"ID: {id_ksiazki}, Wypożyczona przez: {student}")
    print("------------------------")

def zwroc_ksiazke():
    id_ksiazki = int(input("Podaj ID książki do zwrotu: "))
    if id_ksiazki in wypozyczone:
        del wypozyczone[id_ksiazki]
        print("Książka została zwrócona.")
    else:
        print("Ta książka nie jest wypożyczona.")
    print("------------------------")

def pokaz_komendy():
    print("------------------------")
    print("Dostępne komendy:")
    print("1 - dodaj książkę")
    print("2 - dodaj studenta")
    print("3 - wypożycz książkę")
    print("4 - liczba książek (oraz lista)")
    print("5 - liczba wypożyczonych")
    print("6 - zwróć książkę")
    print("7 - pokaż komendy")
    print("exit - wyjście")
    print("------------------------")

pokaz_komendy()
while True:
    komenda = input("Wybierz opcję: ")
    if komenda == "exit":
        break
    elif komenda == "1":
        dodaj_ksiazke()
    elif komenda == "2":
        dodaj_studenta()
    elif komenda == "3":
        wypozycz_ksiazke()
    elif komenda == "4":
        liczba_ksiazek()
    elif komenda == "5":
        liczba_wypozyczonych()
    elif komenda == "6":
        zwroc_ksiazke()
    elif komenda == "7":
        pokaz_komendy()
    else:
        print("Nieznana opcja!")
