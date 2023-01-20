from functools import cmp_to_key

def packet_cmp(l, r):
    ## Cases (possible values that e{1,2} can take is {list, int})

    # list - list
    if type(l) is list and type(r) is list:
        i = 0
        while(i < len(l) and i < len(r)):
            if packet_cmp(l[i], r[i]) == -1:
                return -1
            elif packet_cmp(l[i], r[i]) == 1:
                return 1
            i += 1

        if i == len(l) and i == len(r):
            return 0
        elif i == len(l):
            return -1
        elif i == len(r):
            return 1

    # list - int
    if type(l) is list and type(r) is int:
        r = [r]
        return packet_cmp(l, r)

    # int - list
    if type(l) is int and type(r) is list:
        l = [l]
        return packet_cmp(l, r)

    # int - int
    if type(l) is int and type(r) is int:
        if l < r:
            return -1
        elif l > r:
            return 1
        else:
            return 0

with open("input.txt") as f:
    packets = list()
    while True:
        line = f.readline()
        if line != '' and line != '\n':
            packets.append(eval(line))
        elif line == '':
            break

    packets.append([[2]])
    packets.append([[6]])

    packets = sorted(packets, key=cmp_to_key(packet_cmp))

for l in packets:
    print(l)

i1 = packets.index([[2]])
i2 = packets.index([[6]])
print((i1 + 1)*(i2 + 1))
