# Zum Winde verweht

*J1, Team-ID: 00353, Team-Name: U+1F947, Leonhard Masche, 24.09.2021*

## Inhaltsverzeichnis

1. [Lösungsidee](#lösungsidee)
2. [Umsetzung](#umsetzung)
3. [Beispiele](#beispiele)
4. [Quellcode](#quellcode)

## Lösungsidee

Zuerst bietet es sich an, die Koordinaten der Häuser und der Windräder in Listen zu speichern. Man kann nun mit zwei ineninander verschachtelten for-loops für jedes Windrad und jedes Haus die Entfernung mithilfe des Satz des Pythagoras berechnen. Die kleinste ermittelte Entfernung pro Windrad wird durch 10 geteilt, auf 2 Stellen nach dem Komma gerundet, und zusammen mit den Koordinaten des Windrads ausgegeben.

## Umsetzung

Das Programm ist in der Sprache Python umgesetzt. Der Aufgabenordner enthält neben dieser Dokumentation eine ausführbare Python-Datei. Diese Datei ist mit einer Python-Umgebung ab der Version `3.6` ausführbar.

Wird das Programm gestartet, wird zuerst eine Eingabe in Form einer einstelligen Zahl erwartet, um ein bestimmtes Beispiel auszuwählen. *(Das heißt: `1` für Beispiel `landkreis1.txt`)*

Nun wird die Logik des Programms angewandt und die Ausgabe erscheint in der Kommandozeile.

## Beispiele

Hier wird das Programm auf die vier Beispiele aus dem Git-Repo angewendet:

---

`landkreis1.txt`

```
12 3
-82 -315
248 714
1202 907
226 680
694 -20
-767 44
-245 719
-339 36
473 406
863 -290
953 885
-109 510
1242 -593
-1223 -1479
1720 401
```

Ausgabe zu `landkreis1.txt`

```
Standort (1242|-593): 48.52m
Standort (-1223|-1479): 158.98m
Standort (1720|401): 72.41m
```

---

`landkreis2.txt`

```
94 15
1157 3693
1063 1317
1493 2916
800 2849
1568 3562
    ⋮
3411 2207
1255 3346
1309 3588
2111 2794
1534 3040
359 20
2 -773
315 -213
-629 -532
97 -69
    ⋮
276 292
156 55
-423 -93
202 -219
-340 -343
```

Ausgabe zu `landkreis2.txt`

```
Standort (359|20): 115.16m
Standort (2|-773): 201.25m
Standort (315|-213): 138.85m
Standort (-629|-532): 209.12m
Standort (97|-69): 132.01m
Standort (-392|-418): 186.16m
Standort (87|-384): 161.68m
Standort (-597|612): 133.3m
Standort (-13|-32): 133.54m
Standort (-57|49): 128.77m
Standort (276|292): 91.78m
Standort (156|55): 118.28m
Standort (-423|-93): 161.95m
Standort (202|-219): 142.39m
Standort (-340|-343): 177.04m
```

---

`landkreis3.txt`

```
2382 16
8801 6661
5748 17368
4490 12848
10935 12512
6940 9243
    ⋮
9694 12538
4785 7982
9391 10712
10412 12825
11378 10021
0 0
180 570
360 1140
540 1710
360 -120
    ⋮
1260 1470
1080 -360
1260 210
1440 780
1620 1350
```

Ausgabe zu `landkreis3.txt`

```
Standort (0|0): 451.57m
Standort (180|570): 393.79m
Standort (360|1140): 336.7m
Standort (540|1710): 280.74m
Standort (360|-120): 444.62m
Standort (540|450): 385.71m
Standort (720|1020): 327.11m
Standort (900|1590): 269.02m
Standort (720|-240): 440.84m
Standort (900|330): 381.25m
Standort (1080|900): 321.73m
Standort (1260|1470): 262.32m
Standort (1080|-360): 440.31m
Standort (1260|210): 380.54m
Standort (1440|780): 320.78m
Standort (1620|1350): 261.02m
```

---

`landkreis4.txt`

```
9993 30
-4147 8575
4966 6387
1771 2674
2417 6350
4207 5051
    ⋮
2336 4331
4774 1732
1663 3918
1618 5620
6616 6675
-4147 8575
-6453 14307
-8370 5831
13045 -5404
-8361 8131
    ⋮
-3214 15263
6887 17263
-3944 13584
6576 15697
-12074 5974
```

Ausgabe zu `landkreis4.txt`

```
Standort (-4147|8575): 0.0m
Standort (-6453|14307): 383.81m
Standort (-8370|5831): 262.45m
Standort (13045|-5404): 233.99m
Standort (-8361|8131): 296.19m
Standort (-6963|-371): 71.76m
Standort (9772|-3239): 181.41m
Standort (-5102|-1726): 235.4m
Standort (13454|11822): 343.11m
Standort (-7427|1720): 177.9m
Standort (-7816|12396): 449.16m
Standort (-11095|603): 408.03m
Standort (8314|16301): 317.95m
Standort (15283|-2961): 221.29m
Standort (7082|18552): 520.12m
Standort (16743|2687): 394.71m
Standort (17511|-730): 433.25m
Standort (-10767|12860): 703.83m
Standort (1508|-8030): 168.42m
Standort (-7767|982): 201.27m
Standort (1277|-11294): 139.16m
Standort (-8724|3575): 348.99m
Standort (7033|-7766): 297.91m
Standort (2720|-10910): 110.23m
Standort (20589|7265): 813.6m
Standort (-3214|15263): 236.19m
Standort (6887|17263): 391.94m
Standort (-3944|13584): 125.78m
Standort (6576|15697): 241.01m
Standort (-12074|5974): 625.4m
```

## Quellcode

```python
# pylama:ignore=E501
import math
from os import path


# absoluter Pfad des ausgewählten Beispiels
path = path.join(
    path.dirname(path.abspath(__file__)),
    f'beispieldaten/landkreis{input("Nummer des Beispiels eingeben: ")}.txt')

with open(path, 'r') as f:
    lines = f.read().split('\n')


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
```
