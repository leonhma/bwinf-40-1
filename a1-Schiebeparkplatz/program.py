# pylama:ignore=C901,E501
import string


with open(f'beispieldaten/parkplatz{input("Nummer des Beispiels eingeben: ")}.txt', 'r') as f:
    lines = f.read().split('\n')

spaces = lines[0].split(' ')
letters = list(string.ascii_uppercase)
bounds = (letters.index(spaces[0]), letters.index(spaces[1])+1)
parked = letters[bounds[0]:bounds[1]]

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
        actions = []
    car = get_blocking(space_to_free)
    left, _ = get_movement(car, space_to_free)
    actions.append(f'{car} {left} links')
    if not check_free(blocking[car]-left):
        squash_left(blocking[car]-left, actions)
    return actions


def squash_right(space_to_free, actions=None):
    if not actions:
        actions = []
    car = get_blocking(space_to_free)
    _, right = get_movement(car, space_to_free)
    actions.append(f'{car} {right} rechts')
    if not check_free(blocking[car]+right+1):
        squash_right(blocking[car]+right+1, actions)
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

    # get how many spaces the first blocking car has to move
    car = get_blocking(space)
    if car is not None:
        left, right = get_movement(car, space)

        if left == 1 and buffer_left >= 1:
            output += ', '.join(squash_left(space)[::-1])
        elif right == 1 and buffer_right >= 1:
            output += ', '.join(squash_right(space)[::-1])
        elif buffer_left >= left:
            output += ', '.join(squash_left(space)[::-1])
        elif buffer_right >= right:
            output += ', '.join(squash_right(space)[::-1])
        else:
            output += 'Unmöglich!'

    print(output)
