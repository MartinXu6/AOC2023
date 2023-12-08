Input = [i.strip("\n") for i in open("input.txt", "r")]
total = 0
#p1
# for line in range(len(Input)):
#     current = ""
#     add = False
#     for letter in range(len(Input[line])):
#         checks = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
#         if Input[line][letter].isnumeric():
#             current += Input[line][letter]
#             for check in checks:
#                 if line + check[0] >= 0 and letter + check[1] >= 0 and (line + check[0]) <= len(Input) -1 and letter + check[1] <= len(Input[line]) -1:
#                     if not Input[line + check[0]][letter + check[1]].isnumeric() and Input[line + check[0]][letter + check[1]] != ".":
#                         add = True
#                         break
#         else:
#             if add:
#                 total += int(current)
#                 add = False
#             current = ""
#     if len(current) > 0:
#         if add:
#             total += int(current)
#p2
gears = dict()
for line in range(len(Input)):
    current = ""
    current_gears = set()
    for letter in range(len(Input[line])):
        checks = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        if Input[line][letter].isnumeric():
            current += Input[line][letter]
            for check in checks:
                if line + check[0] >= 0 and letter + check[1] >= 0 and (line + check[0]) <= len(Input) -1 and letter + check[1] <= len(Input[line]) -1:
                    if Input[line + check[0]][letter + check[1]] == "*":
                        current_gears.add((line+check[0],letter + check[1]))
                        gears[(line+check[0],letter + check[1])] = gears.get((line+check[0],letter + check[1]),[])
        else:
            if current:
                for gear in current_gears:
                    gears[gear].append(int(current))
                current_gears = set()
            current = ""
    if len(current) > 0:
        for gear in current_gears:
            gears[gear].append(int(current))
for item in gears:
    if len(gears[item]) == 2:
        total += gears[item][0] * gears[item][1]
print(gears)
print(total)
