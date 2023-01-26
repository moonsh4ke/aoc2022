from collections import namedtuple
import sys

# sensor-beacon pairs
PAIRS = list()
MAX_SIZE = 4_000_000

Data = namedtuple("Data", ["sensor", "beacon", "d"])
Point = namedtuple("Point", ["x", "y"])

# Manhattan distance
def man_dis(p1: Point, p2: Point) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def check_point(p: Point) -> bool:
    for pair in PAIRS:
        if man_dis(p, pair.sensor) <= pair.d:
            return False
    return True

def oor(p: Point) -> bool:
    if p.x < 0 or p.x > MAX_SIZE:
        return True
    if p.y < 0 or p.y > MAX_SIZE:
        return True

with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == "":
            break
        for c in ",:":
            line = line.replace(c, "")
        line = line.split()
        sensor = Point(int(line[2].split("=")[1]), int(line[3].split("=")[1]))
        beacon = Point(int(line[8].split("=")[1]), int(line[9].split("=")[1]))
        d = man_dis(sensor, beacon)
        data = Data(sensor, beacon, d)
        PAIRS.append(data)


# Iterate over all pairs and for each point at d+1 man dis check if it is discarted by other pair
def get_point():
    for pair in PAIRS:
        sensor = pair.sensor
        d = pair.d
        for h in range(d+1):
            dx1 = sensor.x + h
            dx2 = sensor.x - h
            dy1 = d + 1 - h + sensor.y
            dy2 = -d - 1 + h + sensor.y

            p1 = Point(dx1, dy1)
            p2 = Point(dx1, dy2)
            p3 = Point(dx2, dy1)
            p4 = Point(dx2, dy2)

            points = [p1, p2, p3, p4]

            for point in points:
                # Out Of Range point
                if oor(point) == True:
                    continue
                if(check_point(point) == True):
                    return point

b = get_point()
print(b.x * 4_000_000 + b.y)
