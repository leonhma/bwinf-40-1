# pylama:ignore=E501
import math
from os import path


# absoluter Pfad des ausgewählten Beispiels
path = path.join(
    path.dirname(path.abspath(__file__)),
    f'beispieldaten/landkreis{input("Nummer des Beispiels eingeben: ")}.txt')

with open(path, 'r') as f:
    lines = f.read().split('\n')

print('--------------------------------')


# die Koordinaten in Form von Listen (`List`) speichern
n_houses, n_windmills = tuple(lines[0].split(' '))
n_houses, n_windmills = int(n_houses), int(n_windmills)
coords = [(int(line.split(' ')[0]), int(line.split(' ')[1])) for line in lines[1:n_houses+n_windmills+1]]
houses = coords[:n_houses]
windmills = coords[n_houses:]


# über alle Windräder-Standorte iterieren
for w_coord in windmills:
    min_distance = 99999999
    # über alle Häuser iterieren
    for h_coord in houses:
        # Entfernung berechnen. d = sqrt(Δx²+Δy²)
        distance = math.sqrt((w_coord[0]-h_coord[0])**2+(w_coord[1]-h_coord[1])**2)
        if(distance < min_distance):
            min_distance = distance
    print(f'Standort ({w_coord[0]}|{w_coord[1]}): {round(min_distance/10, 2)}m')

print('--------------------------------')
