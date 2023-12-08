Input = [i.strip("\n") for i in open("input.txt", "r")]
total = 0
# p1
# for line in Input:
#     num1 = 0
#     num2 = 0
#     for letter in line:
#         if letter.isnumeric():
#             num1 += int(letter)
#             break
#     for letter in line[::-1]:
#         if letter.isnumeric():
#             num2 += int(letter)
#             break
#     total += num1*10 + num2
# print(total)
# p2
numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
for line in Input:
    first = 0
    last = 0
    num1 = 0
    num2 = 0
    for letter in range(len(line)):
        if line[letter].isnumeric() and int(line[letter]) != 0:
            first = letter
            num1 = int(line[letter])
            break
    for letter in range(len(line)):
        if line[::-1][letter].isnumeric() and int(line[::-1][letter]) != 0:
            last = len(line) - letter - 1
            num2 = int(line[::-1][letter])
            break
    if first == 0 and num1 == 0:
        first = 9999999
    for num in numbers:
        pos = line.find(num)
        if pos > -1:
            if pos < first:
                first = pos
                num1 = numbers[num]
    for num in numbers:
        pos = line.rfind(num)
        if pos > -1:
            if pos > last:
                last = pos
                num2 = numbers[num]
    total += num1 * 10 + num2
print(total)
