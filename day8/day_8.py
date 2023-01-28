def get_score(grid: list, index: tuple) -> int:
    i, j = index
    n = len(grid)
    m = len(grid[0])
    t = b = l = r = 0

    # from top
    for k in range(i-1, -1, -1):
        t += 1
        if grid[k][j] >= grid[i][j]:
            break

    # from bottom
    for k in range(i+1, n):
        b += 1
        if grid[k][j] >= grid[i][j]:
            break
    
    # from left
    for k in range(j-1, -1, -1):
        l += 1
        if grid[i][k] >= grid[i][j]:
            break

    # from right
    for k in range(j+1, m):
        r += 1
        if grid[i][k] >= grid[i][j]:
            break

    return t*b*l*r


def ghs(grid: list) -> int:
    n = len(grid)
    m = len(grid[0])
    max_score = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            score = get_score(grid, (i, j))
            if(score > max_score):
                max_score = score
    return max_score
            

def is_visible(grid: list, index: tuple) -> bool:
    i, j = index
    n = len(grid)
    m = len(grid[0])

    # Check if there's a tree taller in row

    # from top
    for k in range(i):
        if grid[k][j] >= grid[i][j]:
            break
    else:
        return True

    # from bottom
    i, j = index
    for k in range(i+1, n):
        if grid[k][j] >= grid[i][j]:
            break
    else:
        return True
    
    # from left
    for k in range(j):
        if grid[i][k] >= grid[i][j]:
            break
    else:
        return True

    # from right
    i, j = index
    for k in range(j+1, m):
        if grid[i][k] >= grid[i][j]:
            break
    else:
        return True

    return False

# Compute how much visible edges are visible in the grid
def get_visible(grid: list) -> int:
    # Compute edges
    n = len(grid)
    m = len(grid[0])
    ve = n*2 + m*2 - 4 # ve: visible edges
    ie = 0 # ie: inner edges
    for i in range(1, n-1):
        for j in range(1, m-1):
            # Check if inner edge is visible
            if is_visible(grid, (i, j)) == True:
                ie += 1
    return ie+ve

with open("input.txt", "r") as f:
    grid = list() # Matrix
    # Read file as matrix
    while(True):
        line = f.readline()
        if(line == ""):
            break
        grid.append([int(n) for n in line.replace("\n", "")])

# (1)
# Compute visible trees
# vt = get_visible(grid) # vt: visible tree

hs = ghs(grid) # ghs: get hight score
print(hs)
