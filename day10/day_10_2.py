import functools

# his
his = list()

# cicle
cic = 1

# register X
X = 1

# Sprite can be represented as an index
# spr_i: sprite index
spr_i = 0
crt = list()

his.append((cic, X))
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == "":
            break
    
        line = line.split()    

        # instruction, rest
        ins, *res = tuple(line)

        if ins == "addx":
            val = int(res[0])
            for i in range(1, 3):
                cic +=1
                if(i == 2):
                    X += val
                his.append((cic, X))
        else:
            cic += 1
            his.append((cic, X))


k = 0
for i in range(6):
    crt_row = [None] * 40
    for j in range(40):
        # what is the sprite
        _, x = his[k]
        sprite = x
        if(j+1 == x or j+1 == x + 1 or j+1 == x + 2):
            crt_row[j] = "#"
        else:
            crt_row[j] = "."
        k = k + 1
    crt.append(crt_row)

for row in crt:
    print("".join(row))