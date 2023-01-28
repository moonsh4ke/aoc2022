def get_priority(c: str):
    if(ord(c) < 91):
        return ord(c) - 65 + 27
    return ord(c) - 97 + 1

# total_sum = 0
# with open("input.txt", "r") as f:
#     while(True):
#         line = f.readline()
#         if(line == ''):
#             break
#         line.replace("\n", "")
#         left = line[:len(line)//2]
#         right = line[len(line)//2:]
#         print(f"{left}\t{right}")

#         for c in left:
#             if(c in right):
#                 total_sum += get_priority(c)
#                 break


total_sum = 0
with open("input.txt", "r") as f:
    while(True):
        elf1 = f.readline()
        if(elf1 == ''):
            break
        elf2 = f.readline()
        elf3 = f.readline()

        elf1.replace("\n", "")
        elf2.replace("\n", "")
        elf3.replace("\n", "")

        flag = 0
        for e1_c in elf1:
            for e2_c in elf2:
                if e1_c == e2_c:
                    for e3_c in elf3:
                        if e1_c == e3_c:
                            total_sum += get_priority(e1_c)
                            flag = 1
                            break
                    break
            if(flag == 1):
                break

print(total_sum)