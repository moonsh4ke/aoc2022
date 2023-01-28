# Contador de pares
count = 0
# Cargar archivo
with open('input.txt', 'r') as f:
    while(True):
        line = f.readline()
        if line == '':
            break
        line = line.replace("\n", "");
        # par: l1-l2,r1-r2
        #        l     r
        l = line.split(",")[0]
        r = line.split(",")[1]
        l1, l2 = tuple(l.split("-"))
        r1, r2 = tuple(r.split("-"))
        l1, l2 = int(l1), int(l2)
        r1, r2 = int(r1), int(r2)

        ## (1)
        # l esta contenido en r
        # if(l1 >= r1 and l2 <= r2):
        #     count += 1
        # elif(r1 >= l1 and r2 <= l2):
        #     count += 1

        s1 = set(range(l1, l2+1))
        s2 = set(range(r1, r2+1))

        if(s1 & s2 != set()):
            count += 1

print(count)