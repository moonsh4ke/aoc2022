from collections import namedtuple
import sys

# sensor-beacon pairs
PAIRS = list()
ROW = 10

Data = namedtuple("Data", ["sensor", "beacon"])
Point = namedtuple("Point", ["x", "y"])

# Manhattan distance
def man_dis(p1: Point, p2: Point) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

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
        PAIRS.append(data)

left, right = sys.maxsize, -sys.maxsize
for pair in PAIRS:
    sensor = pair.sensor
    beacon = pair.beacon
    # d: distance
    d = man_dis(sensor, beacon)
    if ROW > sensor.y + d or ROW < sensor.y - d:
        continue
    x1 = d - abs(sensor.y - ROW) + sensor.x
    x2 = - d + abs(sensor.y - ROW) + sensor.x
    if min(x1, x2) < left:
        left = min(x1, x2)
    if max(x1,x2) > right:
        right = max(x1, x2)

print(left, right)
# sensor = PAIRS[6].sensor
# beacon = PAIRS[6].beacon
# # d: distance
# d = man_dis(sensor, beacon)

# x1 = d - abs(sensor.y - ROW) + sensor.x
# x2 = - d + abs(sensor.y - ROW) + sensor.x

# if min(x1, x2) < left:
#     left = min(x1, x2)
# if max(x1,x2) > right:
#     right = max(x1, x2)

potential = abs(right - left) + 1

discarted = list()
for pair in PAIRS:
    if pair.beacon.y == ROW and pair.beacon.y in range(left, right + 1) and \
        pair.beacon not in discarted:
        discarted.append(pair.beacon)
        potential -= 1
    if pair.sensor.y == ROW and pair.sensor.y in range(left, right + 1):
        potential -= 1

print(potential)
