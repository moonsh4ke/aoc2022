decrypt = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
shape_val = {'rock': 1, 'paper': 2, 'scissors': 3}

# tijera x papel -> 1, tijera x piedra -> piedra
# papel x tijera -> 0, papel x piedra -> 1
# piedra, tijera -> 1, piedra, papel -> 0

# 1: p1 won, 2: p2 won, 0: draw
def play(p1: str, p2: str) -> int:
    if(p1 == 'scissors'):
        if(p2 == 'paper'):
            return 6
        if(p2 == 'rock'):
            return 0
    if(p1 == 'paper'):
        if(p2 == 'scissors'):
            return 0
        if(p2 == 'rock'):
            return 6
    if(p1 == 'rock'):
        if(p2 == 'scissors'):
            return 6
        if(p2 == 'paper'):
            return 0
    return 3

def get_shape(p2: str, result: str):
    if(p2 == 'rock'):
        if(result == 'X'):
            return 'scissors'
        if(result == 'Y'):
            return p2
        if(result == 'Z'):
            return 'paper'
    if(p2 == 'paper'):
        if(result == 'X'):
            return 'rock'
        if(result == 'Y'):
            return p2
        if(result == 'Z'):
            return 'scissors'
    if(p2 == 'scissors'):
        if(result == 'X'):
            return 'paper'
        if(result == 'Y'):
            return p2
        if(result == 'Z'):
            return 'rock'

# total_score = 0
# (1)
# with open('input.txt', 'r') as f:
#     while(True):
#         line = f.readline()
#         if(line == ""):
#             break
#         # symbol for p1 and p2
#         symbol_1, symbol_2 = line.split()
#         total_score += play(decrypt[symbol_2], decrypt[symbol_1])
#         total_score += shape_val[decrypt[symbol_2]]

total_score = 0
i = 0
with open('input.txt', 'r') as f:
    while(True):
        line = f.readline()
        if(line == ""):
            break
        # symbol for p1 and p2
        symbol_1, symbol_2 = line.split()

        shape = get_shape(decrypt[symbol_1], symbol_2)
        total_score += play(shape, decrypt[symbol_1])
        total_score += shape_val[shape]

print(total_score)