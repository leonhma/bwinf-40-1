# pylama:ignore=E501
class ilist(list):
    def __init__(self, r=None, empty=None):
        if r is None:
            r = []
        list.__init__(self, r)
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


with open(f'beispieldaten/praeferenzen{input("Nummer des Beispiels eingeben: ")}.txt', 'r') as f:
    lines = f.read().split('\n')

n, m = tuple(lines[0].split(' '))
n, m = int(n), int(m)
matrix = []
for line in lines[1:n+1]:
    matrix.append([int(x) for x in line.split(' ')])

neededchanges = ilist(empty=0)
for i in range(m):
    for prefs in matrix:
        if prefs[i] > min(prefs):
            neededchanges[i] += 1

if min(neededchanges) == 0:
    print(
        f'"Allseits beliebter Termin" gefunden: Tag {neededchanges.index(0)+1}.')
else:
    print(
        f'Kein "allseits beliebter Termin" gefunden. {min(neededchanges)} Änderung(en) an Tag {neededchanges.index(min(neededchanges))} benötigt.')
