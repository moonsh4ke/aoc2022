import functools

# his
his = list()

# cicle
cic = 1

# register X
X = 1

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

sum = 0
for c, x in his:
    if c in [20, 60, 100, 140, 180, 220]:
        sum += c * x

print(sum)