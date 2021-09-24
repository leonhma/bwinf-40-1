# pylama:ignore=C901,E501
import string                                                                       # string constants
from os import path                                                                 # path manipulation


path = path.join(
    path.dirname(path.abspath(__file__)),
    f'beispieldaten/parkplatz{input("Nummer des Beispiels eingeben: ")}.txt')       # get the path of the test file

with open(path, 'r') as f:                                                          # open the test file
    lines = f.read().split('\n')

print('--------------------------------')                                           # print a seperator


spaces = lines[0].split(' ')                                                        # get the two outer parking spaces (eg. 'A' and 'C')
letters = list(string.ascii_uppercase)                                              # get a list of alphabetically ordered uppercase letters
bounds = (letters.index(spaces[0]), letters.index(spaces[1])+1)                     # get the indexes of the outermost parking spaces
parked = letters[bounds[0]:bounds[1]]                                               # get a list of all the applicable parking spaces


blocking = dict()
for i in range(int(lines[1])):
    line = lines[2+i]
    blocking[line.split(' ')[0]] = int(line.split(' ')[1])


def get_blocking(space_to_free):
    for x in blocking.items():
        if space_to_free-1 in x:
            return x[0]
    for x in blocking.items():
        if space_to_free in x:
            return x[0]


def check_free(space_to_free):
    if (space_to_free - 1 in blocking.values() or
            space_to_free in blocking.values()):
        return False
    return True


def get_movement(car, space_to_free):
    left = 1
    if(blocking[car] == space_to_free):
        left = 2
    right = 1
    if(blocking[car] == space_to_free-1):
        right = 2
    return left, right


def squash_left(space_to_free, actions=None):
    if not actions:
        actions = [0, []]
    car = get_blocking(space_to_free)
    left, _ = get_movement(car, space_to_free)
    actions[0] += left
    actions[1].append(f'{car} {left} links')
    if not check_free(blocking[car]-left):
        actions = squash_left(blocking[car]-left, actions)
    return actions


def squash_right(space_to_free, actions=None):
    if not actions:
        actions = [0, []]
    car = get_blocking(space_to_free)
    _, right = get_movement(car, space_to_free)
    actions[0] += right
    actions[1].append(f'{car} {right} rechts')
    if not check_free(blocking[car]+right+1):
        actions = squash_right(blocking[car]+right+1, actions)
    return actions


for space, car in enumerate(parked):
    bound_left, bound_right = bounds
    output = f'{car}: '
    # check if not blocked
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
    if car is not None:
        left, right = get_movement(car, space)

        if buffer_left >= left:
            options.append(squash_left(space))
        if buffer_right >= right:
            options.append(squash_right(space))
        options.sort(key=lambda x: x[0])
        output += ', '.join(options[0][1][::-1])

    print(output)

print('--------------------------------')
