# pylama:ignore=C901,E501
import string
from os import path


# absoluter Pfad des ausgewählten Beispiels
path = path.join(
    path.dirname(path.abspath(__file__)),
    f'beispieldaten/parkplatz{input("Nummer des Beispiels eingeben: ")}.txt')

with open(path, 'r') as f:
    lines = f.read().split('\n')


# ausgewählte Test-Datei einlesen
spaces = lines[0].split(' ')
letters = list(string.ascii_uppercase)
bounds = (letters.index(spaces[0]), letters.index(spaces[1])+1)
parked = letters[bounds[0]:bounds[1]]


# dictionary aus blockierenden (querstehenden) Autos erstellen
blocking = dict()
for i in range(int(lines[1])):
    line = lines[2+i]
    blocking[line.split(' ')[0]] = int(line.split(' ')[1])


def get_blocking(i):
    # gibt das Auto, das die Position mit dem index
    # `i` blockiert, zurück. Sonst `None`
    for x in blocking.items():
        if i-1 in x:
            return x[0]
    for x in blocking.items():
        if i in x:
            return x[0]


def check_free(i):
    # gibt `True` zurück, wenn die Position `i`
    # frei ist, sonst `False`
    if (i - 1 in blocking.values() or
            i in blocking.values()):
        return False
    return True


def get_movement(car, i):
    # gibt die Bewegung, die ein Auto `car` machen müsste,
    # um Position `i` freizugeben, zurück
    left = 1
    if(blocking[car] == i):
        left = 2
    right = 1
    if(blocking[car] == i-1):
        right = 2
    return left, right


def squash_left(i, actions=None):
    # Zeichnet rekursiv alle Bewegungen auf, die gemacht werden
    # müssten, um Position `i` nach links freizumachen
    if not actions:
        actions = [0, []]
    car = get_blocking(i)
    left, _ = get_movement(car, i)
    actions[0] += left
    actions[1].append(f'{car} {left} links')
    if not check_free(blocking[car]-left):
        actions = squash_left(blocking[car]-left, actions)
    return actions


def squash_right(i, actions=None):
    # Zeichnet rekursiv alle Bewegungen auf, die gemacht werden
    # müssten, um Position `i` nach rechts freizumachen
    if not actions:
        actions = [0, []]
    car = get_blocking(i)
    _, right = get_movement(car, i)
    actions[0] += right
    actions[1].append(f'{car} {right} rechts')
    if not check_free(blocking[car]+right+1):
        actions = squash_right(blocking[car]+right+1, actions)
    return actions


for space, car in enumerate(parked):
    bound_left, bound_right = bounds
    output = f'{car}: '

    # berechnen, wie viel Platz in jede Richtung frei ist
    buffer_left = 0
    for i in range(bound_left, space):
        if check_free(i):
            buffer_left += 1
    buffer_right = 0
    for i in range(space+1, bound_right):
        if check_free(i):
            buffer_right += 1

    options = []
    car = get_blocking(space)
    # wenn dieser Parkplatz blockiert ist,
    if car is not None:
        left, right = get_movement(car, space)
        # dann vergleiche das Verschieben nach
        if buffer_left >= left:
            # links
            options.append(squash_left(space))
        # mit dem Verschieben nach
        if buffer_right >= right:
            # rechts
            options.append(squash_right(space))
        # wähle die seite mit den wenigsten Bewegungen aus
        options.sort(key=lambda x: x[0])
        # drehe die Liste der Aktionen um, um Kollisionen zu vermeiden
        output += ', '.join(options[0][1][::-1])

    print(output)
