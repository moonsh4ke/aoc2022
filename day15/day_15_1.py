from collections import namedtuple

N = M = 2000000
ORIGIN = 50, 50

# Sensor map
SMAP = [["."] * M for _ in range(N)]

SENSORS = list()

Data = namedtuple("Data", ["sensor", "beacon"])
Point = namedtuple("Point", ["x", "y"])

# Manhattan distance
def man_dis(p1: Point, p2: Point) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def discart(data: Data):
    closest_dist = man_dis(data.beacon, data.sensor)
    for i in range(N):
        for j in range(M):
            if SMAP[i][j] != "S" and \
            data.beacon != Point(i - ORIGIN[0], j - ORIGIN[1])  and \
            man_dis(Point(i - ORIGIN[0], j - ORIGIN[1]), data.sensor) <= closest_dist:
                SMAP[i][j] = "#"


def debug_map():
    for j in range(-2, 23):
        for i in range(-1, 26):
            print(SMAP[ORIGIN[0] + i][ORIGIN[1] + j], end="")
        print()
    print()


def draw_map():
    for data in SENSORS:
        SMAP[ORIGIN[0] + data.sensor.x][ORIGIN[1] + data.sensor.y] = "S"
        SMAP[ORIGIN[0] + data.beacon.x][ORIGIN[1] + data.beacon.y] = "B"


with open("test.txt") as f:
    while True:
        line = f.readline()
        if line == "":
            break
        for c in ",:":
            line = line.replace(c, "")
        line = line.split()
        sensor = Point(int(line[2].split("=")[1]), int(line[3].split("=")[1]))
        beacon = Point(int(line[8].split("=")[1]), int(line[9].split("=")[1]))
        data = Data(sensor, beacon)
        SENSORS.append(data)

draw_map()
# debug_map()

# Example
# discart(SENSORS[6])

# debug_map()

# for data in SENSORS:
#     discart(data)


for data in SENSORS:
    closest_dist = man_dis(data.beacon, data.sensor)
    for j in range(M):
        if SMAP[i][ORIGIN[1] + 10] != "#" and \
        man_dis(SMAP[i][ORIGIN[1] + 10], data.sensor) >= closest_dist:
            SMAP[i][ORIGIN[1] + 10] = "#"

pos = 0
for i in range(N):
    if SMAP[i][ORIGIN[1] + 10] == "#":
        pos += 1

print(pos)
