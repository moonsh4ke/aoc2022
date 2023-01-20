import sys

# Update de shortest path to cell
def update_cell(tovisit: list, hmap: list, path: list, fromm: tuple, to: tuple):
    i, j = fromm
    k, l = to
    if k < 0 or l < 0:
        return
    try:
        if hmap[k][l] != 'v' and \
                hmap[i][j] != 'v' and \
                hmap[k][l] - hmap[i][j] <= 1:
            if path[i][j] + 1 < path[k][l]:
                path[k][l] = path[i][j] + 1
                tovisit.append(to)
    except IndexError:
        return

def print_map(map: list):
    for row in map:
        print(row)

def height_to_number(c: str) -> int:
    if c != 'S' and c != 'E':
        return ord(c)
    elif c == 'S':
        return ord('a')
    elif c == 'E':
        return ord('z')

map = list()
hmap = list()

with open("input.txt", "r") as f:
    # Leer input como una matriz
    while True:
        line = f.readline()
        if line == "":
            break
        line = line.replace("\n", "")
        row = list()
        for c in line:
            row.append(c)
        map.append(row)

# Find S and E positions and set S as a
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "S":
            map[i][j] = 'a'
        elif map[i][j] == "E":
            e = i, j


# aes: list of indices where 'a' is found
aes = list()
for i in range(len(map)):
    for j in range(len(map)):
        if map[i][j] == 'a':
            aes.append((i, j))

evalues = list()
for a in aes:
    # Make a height map
    hmap = [[0] * len(map[0]) for _ in range(len(map))]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "S": hmap[i][j] = ord('a')
            elif map[i][j] == "E":
                hmap[i][j] = ord('z')
            else:
                hmap[i][j] = ord(map[i][j])

    ## Apply Dijkstra starting at position s

    # Make a matrix with path's cost. Initial state is setting startint point to 0 cost
    # And all others are going to be infinite (-1)
    path = [[sys.maxsize] * len(map[0]) for _ in range(len(map))]
    i, j = a
    path[i][j] = 0

    tovisit = list()
    tovisit.append(a)

    # Mientras haya celdas por visitar
    while tovisit != list():
        i, j = tovisit.pop()
        update_cell(tovisit, hmap, path, (i, j), (i - 1, j))
        update_cell(tovisit, hmap, path, (i, j), (i, j + 1))
        update_cell(tovisit, hmap, path, (i, j), (i + 1, j))
        update_cell(tovisit, hmap, path, (i, j), (i, j - 1))
        tovisit = sorted(tovisit, key=lambda x: path[x[0]][x[1]], reverse=True)
        hmap[i][j] = 'v'

    i, j = e
    evalues.append(path[i][j])

print(min(evalues))
