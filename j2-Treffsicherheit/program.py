# pylama:ignore=E501
from os import path

# absoluter Pfad des ausgewählten Beispiels
path = path.join(
    path.dirname(path.abspath(__file__)),
    f'beispieldaten/praeferenzen{input("Nummer des Beispiels eingeben: ")}.txt')

with open(path, 'r') as f:
    lines = f.read().split('\n')


# Datenklasse aus meinem 'brainfuck' interpreter
class ilist(list):
    def __init__(self, start=None, empty=None):
        if start is None:
            start = []
        list.__init__(self, start)
        self.empty = empty

    def _ensure_length(self, n):
        maxindex = n
        if isinstance(maxindex, slice):
            maxindex = maxindex.indices(len(self))[1]
        while len(self) <= maxindex:
            self.append(self.empty)

    def __getitem__(self, n):
        self._ensure_length(n)
        return super(ilist, self).__getitem__(n)

    def __setitem__(self, n, val):
        self._ensure_length(n)
        return super(ilist, self).__setitem__(n, val)


# die Datei einlesen
n, m = tuple(lines[0].split(' '))
n, m = int(n), int(m)
matrix = []
for line in lines[1:n+1]:
    matrix.append([int(x) for x in line.split(' ')])


# durch die Tage iterieren
neededchanges = ilist(empty=0)
for i in range(m):
    for prefs in matrix:
        # Anzahl der Änderungen wird inkrementiert,
        # wenn die Bewertung dieses Tages schlechter
        # als die beste dieses Mitglieds ist
        if prefs[i] > min(prefs):
            neededchanges[i] += 1

# Ausgabe-Logik
changes = min(neededchanges)
if changes == 0:
    print(
        f'"Allseits beliebter Termin" gefunden: Tag {neededchanges.index(0)+1}.')
else:
    print(
        f'Kein "allseits beliebter Termin" gefunden. {changes} Änderung(en) an Tag {neededchanges.index(changes)+1} benötigt.')
