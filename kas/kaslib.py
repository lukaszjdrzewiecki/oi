import random
import math

# Można zmienić te wartości.
N = 1_000_000_000_000_000_000
bajtalary = 10_000_000

# Aby zmienić losowość należy zamienić 1 na dowolną inną liczbę typu int.
rng = random.Random(1)

X = None
czy_zainicjalizowany = False
wygrane = 0

def wylosuj_liczbe():
    return rng.randint(1, N)

def inicjalizuj_gre():
    global X
    X = wylosuj_liczbe()

def inicjalizuj_interakcje():
    global czy_zainicjalizowany
    if czy_zainicjalizowany:
        return
    inicjalizuj_gre()
    czy_zainicjalizowany = True

def proba_zakonczenia():
    if bajtalary <= 0:
        print(f"Liczba wygranych: {wygrane}")
        exit(0)

def zjedz_bajtalara():
    global bajtalary
    proba_zakonczenia()
    bajtalary -= 1

def DajN():
    inicjalizuj_interakcje()
    return N

def Pytaj(y):
    inicjalizuj_interakcje()
    assert 1 <= y <= N
    zjedz_bajtalara()
    proba_zakonczenia()
    return math.gcd(X, y)

def Szturchnij():
    inicjalizuj_interakcje()
    zjedz_bajtalara()
    global X
    X = wylosuj_liczbe()
    proba_zakonczenia()

def Odpowiedz(y):
    inicjalizuj_interakcje()
    assert 1 <= y <= N
    zjedz_bajtalara()
    global wygrane
    assert X == y
    wygrane += 1
    proba_zakonczenia()
    inicjalizuj_gre()
