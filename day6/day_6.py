def get_index(c: str, string: list) -> int:
    for i in range(len(string)):
        if(c == string[i]):
            return i

with open("input.txt") as f:
    signal = f.readline()
    
dinamic_list = [None] * len(signal)

index = -1

dinamic_list[0] = list(signal[0])

for i in range(1, len(signal)):
    if signal[i] not in dinamic_list[i-1]:
        dinamic_list[i] = dinamic_list[i-1] + list(signal[i])
        if(len(dinamic_list[i]) == 14):
            index = i + 1
            break 
    else:
        j = get_index(signal[i], dinamic_list[i-1])
        dinamic_list[i] = dinamic_list[i-1][j+1:] + list(signal[i])


print(index)