# Berechnet die kleinste und die größte Primzahl mit ANZAHL_STELLEN
# Führt eine Zerlegung in Primfaktoren durch
from time import process_time
import math

# Ab hier müssen Sie tätig werden
'''Die kleinste Primzahl, welche die vorgegebene Anzahl Stellen hat,
   soll berechnet werden.
'''
def berechneKleinstePrimzahl(anzStellen):
    pass

'''Die größte Primzahl, welche die vorgegebene Anzahl Stellen hat,
   soll berechnet werden.
'''
def berechneGroesstePrimzahl(anzStellen):
    pass

''' Eine Zahl >=2 soll in ihre Primfaktoren zerlegt werden. Alle Faktoren werden in einer
    Liste zurückgegeben. Achten Sie bitte darauf, dass 1 nicht in der Liste erscheint!
'''
def berechnePrimfaktoren(zahl):
    pass


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
print(f"Primfaktoren von {x}:", berechnePrimfaktoren(9999999999999997))
endzeit = process_time()
print("Rechenzeit Primfaktorzerlegung:", endzeit-startzeit)
