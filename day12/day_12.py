HEIGHT_MAP = list()

# values:
# 0: non visited
# 1: cell is a path
# 2: cell to visit
# 3: dead cell
PATHS = list()

def jumpeable(current: tuple, adjacent: tuple) -> bool:
    i, j = current
    k, l = adjacent
    current = HEIGHT_MAP[i][j]
    # If adjacent is not indexeable, then current is a limit, so return false
    try:
        adjacent = HEIGHT_MAP[k][l]
    except IndexError:
        return False
    return (ord(adjacent) - ord(current)) < 2 and PATHS[k][l] == 0

def pp ():
    for row in PATHS:
        print(row)

def ph ():
    for row in HEIGHT_MAP:
        print(row)


stack = list()

with open("test1.txt", "r") as f:
    while(True):
        line = f.readline()
        if line == "":
            break
        line = line.replace("\n", "")
        HEIGHT_MAP.append([letter for letter in line])

# Search for start
for i in range(len(HEIGHT_MAP)):
    for j in range(len(HEIGHT_MAP[0])):
        if HEIGHT_MAP[i][j] == "S":
            HEIGHT_MAP[i][j] = "a"
            start = i, j
        elif HEIGHT_MAP[i][j] == "E":
            HEIGHT_MAP[i][j] = "z"
            end = i, j

PATHS = [[0] * len(HEIGHT_MAP[0]) for _ in range(len(HEIGHT_MAP))]

# Search for paths
stack.append(start)
while(len(stack) > 0):
    current = stack.pop()
    i, j = current
    top = i - 1, j
    right = i, j + 1
    bottom = i + 1, j
    left = i, j - 1

    k, l = top
    if jumpeable(current, top) == True:
        PATHS[k][l] = 2
        stack.append(top)
    else:
        try:
            if PATHS[k][l] != 1 and PATHS[k][l] != 2:
                PATHS[k][l] = 3
        except IndexError:
            pass
    k, l = right
    if jumpeable(current, right) == True:
        PATHS[k][l] = 2
        stack.append(right)
    else:
        try:
            if PATHS[k][l] != 1 and PATHS[k][l] != 2:
                PATHS[k][l] = 3
        except IndexError:
            pass
    k, l = bottom
    if jumpeable(current, bottom) == True:
        PATHS[k][l] = 2
        stack.append(bottom)
    else:
        try:
            if PATHS[k][l] != 1 and PATHS[k][l] != 2:
                PATHS[k][l] = 3
        except IndexError:
            pass
    k, l = left
    if jumpeable(current, left) == True:
        PATHS[k][l] = 2
        stack.append(left)
    else:
        try:
            if PATHS[k][l] != 1 and PATHS[k][l] != 2:
                PATHS[k][l] = 3
        except IndexError:
            pass

    PATHS[i][j] = 1