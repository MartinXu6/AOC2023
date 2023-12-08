from math import lcm
Input = [i.strip("\n") for i in open("input.txt", "r")]
#p1
# instructions = Input[0]
# connections = dict()
# for line in Input[2:]:
#     connections[line[:3]] = [line[7:10],line[12:15]]
# current = "AAA"
# total =0
# loops = 0
# while True:
#     loops += 1
#     for instruction in instructions:
#         if instruction == "L":
#             current = connections[current][0]
#         else:
#             current = connections[current][1]
#         total += 1
#         if current == "ZZZ":
#             print(total)
#             exit()
#p2
instructions = Input[0]
connections = dict()
for line in Input[2:]:
    connections[line[:3]] = [line[7:10],line[12:15]]
loops = 0
total = []
for start in connections:
    if start[-1] == "A":
        current = start
        summation = 0
        state = True
        while state:
            loops += 1
            for instruction in instructions:
                if instruction == "L":
                    current = connections[current][0]
                else:
                    current = connections[current][1]
                summation += 1
                if current[-1] == "Z":
                    total.append(summation)
                    state = False
                    break
print(connections)
print(lcm(*total))
