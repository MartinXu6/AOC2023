from numpy import prod
times = [54, 81, 70, 88]
Distance = [446, 1292, 1035, 1007]
total = []
#p1
# for time in range(4):
#     current = 0
#     for i in range(times[time] + 1):
#         if i * (times[time] - i) > Distance[time]:
#             current += 1
#     total.append(current)
#p2
total = 0
for i in range(54817089):
        if i * (54817088 - i) > 446129210351007:
             total += 1
print(total)
