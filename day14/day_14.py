N = 1000
M = 1000
START_PT = 500, 0
CAVERN_MAP = [["."] * M for _ in range(N)]

def rest(sand: tuple) -> str:
    x, y = sand
    if CAVERN_MAP[x][y + 1] not in ["#", "o"]:
        sand = x, y + 1
        return "bottom"
    elif CAVERN_MAP[x - 1][y + 1] not in ["#", "o"]:
        sand = x - 1, y + 1
        return "left"
    elif CAVERN_MAP[x + 1][y + 1] not in ["#", "o"]:
        sand = x + 1, y + 1
        return "right"
    return "rested"


def debug_map():
    for j in range(12):
        for i in range(489, 508):
            print(CAVERN_MAP[i][j], end="")
        print("")


def draw_map(paths: list):
    for path in paths:
        for i, point in enumerate(path):
            if i == 0:
                x0, y0 = point
                CAVERN_MAP[x0][y0] = "#"
                continue
            x1, y1 = point

            # Vertical move
            if x0 - x1 < 0:
                for row in CAVERN_MAP[x0:x1+1]:
                    row[y0] = "#"
            elif x0 - x1 > 0:
                for row in CAVERN_MAP[x0:x1-1:-1]:
                    row[y0] = "#"

            # Horizontal move
            elif y0 - y1 < 0:
                CAVERN_MAP[x0][y0+1:y1+1] = ["#"] * abs(y0 - y1)
            elif y0 - y1 > 0:
                CAVERN_MAP[x0][y0-1:y1-1:-1] = ["#"] * abs(y0 - y1)

            x0, y0 = x1, y1


paths = list()
with open("input.txt") as f:
    # starting point
    while True:
        line = f.readline()
        if line == "":
            break
        clean_line = list()
        line = line.split("->")
        for coor in line:
            x, y = coor.split(",")
            x, y = int(x), int(y)
            clean_line.append((x,y))
        paths.append(clean_line)


draw_map(paths)

# Get the floor of the cave
maxj = -1
for i in range(N):
    for j in range(M):
        if CAVERN_MAP[i][j] == "#":
            if j > maxj:
                maxj = j

maxj += 2
# 0 represent air at bottom
for i in range(N):
    CAVERN_MAP[i][maxj] = "#"


rested_sand = 0
while(True):
    sand = START_PT
    if rest(sand) == "rested":
        x, y = sand
        CAVERN_MAP[x][y] = "o"
        rested_sand += 1
        break
    while True:
        x, y = sand
        if rest(sand) == "rested":
            CAVERN_MAP[x][y] = "o"
            rested_sand += 1
            break
        elif rest(sand) == "bottom":
            sand = x, y + 1
            continue
        elif rest(sand) == "left":
            sand = x - 1, y + 1
            continue
        elif rest(sand) == "right":
            sand = x + 1, y + 1
            continue

# set start
# debug_map()
print(rested_sand)
