import functools
max = [0] * 3
with open("input.txt", "r") as f:
    line = f.readline()
    sum = 0
    while line != "":
        if line != "\n":
            sum += int(line)
        else:
            # casos
            # si es mayor que el primero el primero y el segundo se mueven y sum ocupa el primer puesto
            # si es mayor que el segundo, pero menor que el primero, muevo el segundo al tercero y sum ocupa el segundo
            # si es mayor que el tercero, solo intercambio sum con el tercero

            if(sum > max[0]):
                max[2] = max[1]
                max[1] = max[0]
                max[0] = sum
            elif(sum > max[1]):
                max[2] = max[1]
                max[1] = sum
            elif(sum > max[2]):
                max[2] = sum
            sum = 0
        line = f.readline()
    if(sum > max[0]):
        max[2] = max[1]
        max[1] = max[0]
        max[0] = sum
    elif(sum > max[1]):
        max[2] = max[1]
        max[1] = sum
    elif(sum > max[2]):
        max[2] = sum
    print(functools.reduce(lambda x,y: x+y, max))