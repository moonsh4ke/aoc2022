from typing import Callable

class Monkey():
    def __init__(self, si: list, operator: str, number: str, tst_number: int, throw1: int, throw2: int):
        self.items = si
        self.op = lambda old: eval(f"old {operator} {number}")
        self.tst_number = tst_number
        self.tst = lambda w: throw1 if w % tst_number == 0 else throw2
        self.ins = 0

def throw_items(m: Monkey, mod: int):
    for item in m.items:
        # print(f"current worry level is {item}")
        worry = m.op(item) % mod
        # print(f"worry level update to {worry}")
        mon_index = m.tst(worry)
        # print(f"item with worry level {worry} throwed to monkey{mon_index}")
        ml[mon_index].items.append(worry)
        m.ins += 1
    m.items = list()


# ml: monkey list
ml = list()

with open("input.txt", "r") as f:
    while(True):
        line = f.readline()
        if(line == ''):
            break

        mm = list()
        for _ in range(5):
            line = f.readline()
            mm.append(line)

        # transform items to list
        si_line = mm[0][18:]
        si_line = si_line.split(", ")
        si = [int(n) for n in si_line]

        # transform operation into a function
        operation_line = mm[1].split()
        operator, op_number = operation_line[-2], operation_line[-1]

        # test function
        tst_number = int(mm[2].split()[-1])
        throw1 = int(mm[3].split()[-1])
        throw2 = int(mm[4].split()[-1])

        ml.append(Monkey(si, operator, op_number, tst_number, throw1, throw2))
        f.readline()


# for i in range(len(ml)):
#     # print(ml[i].items)

# Computing mod

mod = 1
for monkey in ml:
    mod *= monkey.tst_number

for _ in range(10000):
    for i in range(len(ml)):
        throw_items(ml[i], mod)
    
ins_list = list()
for i in range(len(ml)):
        ins_list.append(ml[i].ins)

ins_list.sort(reverse=True)
print(ins_list)
print(ins_list[0] * ins_list[1])
