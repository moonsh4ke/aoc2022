def is_touching(head: tuple, tail: tuple) -> bool:
    hi, hj = head
    ti, tj = tail

    # Cases
    if hi == ti - 1 and hj == tj - 1:
        return True
    if hi == ti - 1 and hj == tj:
        return True
    if hi == ti - 1 and hj == tj + 1:
        return True
    if hi == ti and hj == tj -1:
        return True
    if hi == ti and hj == tj:
        return True
    if hi == ti and hj == tj + 1:
        return True
    if hi == ti + 1 and hj == tj - 1:
        return True
    if hi == ti + 1 and hj == tj:
        return True
    if hi == ti + 1 and hj == tj + 1:
        return True

    return False

def update_head(cur_pos: tuple, dir: str) -> tuple:
    i, j = cur_pos

    if dir == "U":
        return i-1, j
    if dir == "R":
        return i, j+1
    if dir == "D":
        return i+1, j
    if dir == "L":
        return i, j-1

def update_tail(head: tuple, tail: tuple) -> tuple:
    hi, hj = head
    ti, tj = tail

    if hi == ti - 2 and hj == tj:
        return ti - 1, tj
    if hi == ti - 2 and hj == tj + 1:
        return ti - 1, tj + 1
    if hi == ti - 2 and hj == tj + 2:
        return ti - 1, tj + 1
    if hi == ti - 1 and hj == tj + 2:
        return ti - 1, tj + 1
    if hi == ti and hj == tj + 2:
        return ti, tj + 1
    if hi == ti + 1 and hj == tj + 2:
        return ti + 1, tj + 1
    if hi == ti + 2 and hj == tj + 2:
        return ti + 1, tj + 1
    if hi == ti + 2 and hj == tj + 1:
        return ti + 1, tj + 1
    if hi == ti + 2 and hj == tj:
        return ti + 1, tj
    if hi == ti + 2 and hj == tj - 1:
        return ti + 1, tj - 1
    if hi == ti + 2 and hj == tj - 2:
        return ti + 1, tj - 1
    if hi == ti + 1 and hj == tj - 2:
        return ti + 1, tj - 1
    if hi == ti and hj == tj - 2:
        return ti , tj - 1
    if hi == ti - 1 and hj == tj - 2:
        return ti - 1 , tj - 1
    if hi == ti - 2 and hj == tj - 2:
        return ti - 1, tj - 1
    if hi == ti - 2 and hj == tj - 1:
        return ti - 1 , tj - 1
    

# dimension of matrix
n = 1000   
# matrix
grid = [[None] * n for _ in range(n)]

# start is the center (si, sj), and (xi, xj) is the current pos of head and tail
ti = hi = si = n//2
tj = hj = sj = n//2
# visit count
vc = 1
grid[ti][tj] = "#"

# all start in the same pos
knots = [(hi, hj)] * 10

# Read input
with open("input.txt", "r") as f:
    while(True):
        line = f.readline()
        # EOF
        if(line == ""):
            break

        ## Parse it
        
        line = line.split()
        dir, mov = tuple(line)
        mov = int(mov)

        # (1)
        # for _ in range(mov):
        #     hi, hj = update_head((hi,hj), dir)
        #     # print((hi, hj), (ti, tj))

        #     ## I have to figure out if tail needs to move if so where...
        #     if is_touching((hi, hj), (ti, tj)) == False:
        #         ## fix new tail position
        #         ti, tj = update_tail((hi, hj), (ti, tj))
        #         if grid[ti][tj] != "#":
        #             vc += 1
        #             grid[ti][tj] = "#"

        # (2)
        for _ in range(mov):
            knots[0] = update_head(knots[0], dir)

            # knots copy
            kc = knots.copy()
            for i in range(1, len(kc)):
                # print(f"comparing is touching {knots[i-1]}, {knots[i]}")
                if is_touching(knots[i-1], kc[i]):
                    break
                # print(f"Current knot: {knots[i]}")
                knots[i] = update_tail(knots[i-1], knots[i])
                # print(f"Updated to: {knots[i]}")

            # print(knots)
        
            # last indices
            li, lj = knots[-1]
            if grid[li][lj] != "#":
                vc += 1
                grid[li][lj] = "#"

        # print(" ---------------------------------- ")
            


print(vc)