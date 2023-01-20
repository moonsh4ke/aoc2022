def check_order(l, r):
    ## Cases (possible values that e{1,2} can take is {list, int})

    # list - list
    if type(l) is list and type(r) is list:
        i = 0
        while(i < len(l) and i < len(r)):
            if check_order(l[i], r[i]) == -1:
                return -1
            elif check_order(l[i], r[i]) == 1:
                return 1
            i += 1
        if i == len(l):
            return -1
        return 1

    # list - int
    if type(l) is list and type(r) is int:
        r = [r]
        return check_order(l, r)

    # int - list
    if type(l) is int and type(r) is list:
        l = [l]
        return check_order(l, r)

    # int - int
    if type(l) is int and type(r) is int:
        if l < r:
            return -1
        elif l > r:
            return 1
        else:
            return 0

with open("input.txt") as f:
    index = 0
    sum = 0
    debug = list()
    while True:
        index +=1
        line = f.readline()
        if line == '':
            break

        ## Parsing pairs

        # p{1,2} pairs 1 and 2
        p1 = eval(line)
        p2 = eval(f.readline())
        f.readline() # read next blank line or EOF

        if check_order(p1, p2) in [0, -1]:
            sum += index
            debug.append(index)

print(sum)
# print(debug)
