# Berechnet die kleinste und die größte Primzahl mit ANZAHL_STELLEN
# Führt eine Zerlegung in Primfaktoren durch
from time import process_time
import math

# Ab hier müssen Sie tätig werden
'''Die kleinste Primzahl, welche die vorgegebene Anzahl Stellen hat,
   soll berechnet werden.
'''
def berechneKleinstePrimzahl(anzStellen):
    for i in range(10**(anzStellen-1), 10**anzStellen):
        if len(berechnePrimfaktoren(i)) == 1:
            return i


'''Die größte Primzahl, welche die vorgegebene Anzahl Stellen hat,
   soll berechnet werden.
'''
def berechneGroesstePrimzahl(anzStellen):

    for i in reversed(range(10**(anzStellen-1), 10**anzStellen)):
        if len(berechnePrimfaktoren(i)) == 1:
            return i


''' Eine Zahl >=2 soll in ihre Primfaktoren zerlegt werden. Alle Faktoren werden in einer
    Liste zurückgegeben. Achten Sie bitte daraus, dass 1 nicht in der Liste erscheint.
'''
def berechnePrimfaktoren(zahl):
    faktoren = []
    while zahl % 2 == 0:
      faktoren.append(2),
      zahl = zahl / 2

    for i in range (3, int(math.sqrt(zahl)) + 1, 2):
        while (zahl % i == 0):
            faktoren.append(i)
            zahl = zahl / i

    if zahl > 2:
        faktoren.append(zahl)
    #return set(faktoren)
    return faktoren

# Ab hier kommt ein vorgegebener Programmrahmen, die Daten können sich ändern
ANZAHL_STELLEN = 16

startzeit = process_time()

kp = berechneKleinstePrimzahl(ANZAHL_STELLEN)

zwischenzeit = process_time()

gp = berechneGroesstePrimzahl(ANZAHL_STELLEN)

endzeit = process_time()

print("Kleinste Primzahl:", kp)
print("Berechnungszeit:", zwischenzeit-startzeit)

print("\nGrößte Primzahl:", gp)
print("Berechnungszeit:", endzeit-zwischenzeit)

print("\nGesamte Rechenzeit:", endzeit-startzeit)
x = 9999999999999997
startzeit = process_time()
#print(f"Primfaktoren von {x}:", berechnePrimfaktoren(9999999999999997))
#print(f"Primfaktoren von {x}:", primfak(9999999999999997))
endzeit = process_time()
print("Rechenzeit Primfaktorzerlegung:", endzeit-startzeit)

