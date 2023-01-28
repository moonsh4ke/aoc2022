with open('input.txt', 'r') as f:
    line = f.readline()
    n = len(line) // 4
    stack_list = [list() for i in range(n+1)]

    for i in range(0, n*4, 4):
        crate_str = line[i:i+4]
        for c in "[] \n":
            crate_str = crate_str.replace(c, "")
        if(crate_str != ''):
            stack_list[i//4 + 1].insert(0, crate_str)

    # Stacks are created
    while(True):
        line = f.readline()
        if("[" not in line):
            break

        for i in range(0, n*4, 4):
            crate_str = line[i:i+4]
            for c in "[] \n":
                crate_str = crate_str.replace(c, "")
            if(crate_str != ''):
                stack_list[i//4 + 1].insert(0, crate_str)

    # read space
    f.readline()

    while(True):
        line = f.readline()
        # number of stacks
        if(line == ''):
            break

        line = line.split()
        _, quantity, _, index, _, dest = tuple(line)
        quantity = int(quantity)
        index = int(index)
        dest = int(dest)


        stack_list[dest] += stack_list[index][-quantity:]
        stack_list[index] = stack_list[index][:-quantity]

    out_str = ""
    for i in range(1, n+1):
        if(stack_list[i] != list()):
            out_str += stack_list[i][-1]
            
    print(out_str)