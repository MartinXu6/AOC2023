from collections import Counter
Input = [i.strip("\n") for i in open("input.txt", "r")]
#p1
# five = []
# four = []
# full = []
# three = []
# two_pair = []
# one_pair = []
# high_card = []
#
#
# def give_value(card):
#     return(
#         {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 9, "9": 10, "T": 11, "J": 12, "Q": 13, "K": 14, "A": 15}[
#             card])
#
#
# def sort_cards(cards):
#     total = []
#     cards.sort(key=lambda x: give_value(x[0]))
#     for num in ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]:
#         current1 = sorted([i for i in cards if i[0] == num],key=lambda x: give_value(x[1]))
#         for num1 in ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]:
#             current2 = sorted([x for x in current1 if x[1] == num1],key=lambda x: give_value(x[2]))
#             for num2 in ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]:
#                 current3 = sorted([x for x in current2 if x[2] == num2],key=lambda x: give_value(x[3]))
#                 for num3 in ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]:
#                     current4 = sorted([x for x in current3 if x[3] == num3],key=lambda x: give_value(x[4]))
#                     total += current4
#     return total
#
#
#
#
# for line in Input:
#     line = line.split()
#     hand = line[0]
#     if len(set(hand)) == 1:
#         five.append(hand)
#     elif len(set(hand)) == 2:
#         if hand.count(list(set(hand))[0]) == 1 or hand.count(list(set(hand))[0]) == 4:
#             four.append(hand)
#         else:
#             full.append(hand)
#     elif len(set(hand)) == 3:
#         for letter in hand:
#             if hand.count(letter) == 3:
#                 three.append(hand)
#             elif hand.count(letter) == 2:
#                 two_pair.append(hand)
#     elif len(set(hand)) == 4:
#         one_pair.append(hand)
#     else:
#         high_card.append(hand)
# bids = dict()
# for line in Input:
#     line = line.split()
#     bids[line[0]] = line[1]
# ans = []
# real_ans = 0
# for lists in [high_card,one_pair,two_pair,three,full,four,five]:
#     wanted = []
#     now = sort_cards(lists)
#     for item in now:
#         if item not in wanted:
#             wanted.append(item)
#     ans += wanted
# print(bids)
# for yep in range(1000):
#     real_ans += int(bids[ans[yep]]) * (yep + 1)
# print(real_ans)
#p2
five = []
four = []
full = []
three = []
two_pair = []
one_pair = []
high_card = []


def give_value(card):
    return(
        {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 9, "9": 10, "T": 11, "J": 0, "Q": 13, "K": 14, "A": 15}[
            card])


def sort_cards(cards):
    total = []
    cards.sort(key=lambda x: give_value(x[0]))
    for num in ["J","2","3","4","5","6","7","8","9","T","Q","K","A"]:
        current1 = sorted([i for i in cards if i[0] == num],key=lambda x: give_value(x[1]))
        for num1 in ["J","2","3","4","5","6","7","8","9","T","Q","K","A"]:
            current2 = sorted([x for x in current1 if x[1] == num1],key=lambda x: give_value(x[2]))
            for num2 in ["J","2","3","4","5","6","7","8","9","T","Q","K","A"]:
                current3 = sorted([x for x in current2 if x[2] == num2],key=lambda x: give_value(x[3]))
                for num3 in ["J","2","3","4","5","6","7","8","9","T","Q","K","A"]:
                    current4 = sorted([x for x in current3 if x[3] == num3],key=lambda x: give_value(x[4]))
                    total += current4
    return total




for line in Input:
    line = line.split()
    hand = line[0]
    if hand != "JJJJJ":
        most_frequent = sorted([x for x in hand if x != 'J'],key = lambda x:hand.count(x),reverse=True)[0]
        hand1 = hand.replace("J", most_frequent)
    else:
        hand1 = "JJJJJ"
    if len(set(hand1)) == 1:
        five.append(hand)
    elif len(set(hand1)) == 2:
        if hand1.count(list(set(hand1))[0]) == 1 or hand1.count(list(set(hand1))[0]) == 4:
            four.append(hand)
        else:
            full.append(hand)
    elif len(set(hand1)) == 3:
        for letter in hand1:
            if hand1.count(letter) == 3:
                three.append(hand)
            elif hand1.count(letter) == 2:
                two_pair.append(hand)
    elif len(set(hand1)) == 4:
        one_pair.append(hand)
    else:
        high_card.append(hand)
bids = dict()
for line in Input:
    line = line.split()
    bids[line[0]] = line[1]
ans = []
real_ans = 0
for lists in [high_card,one_pair,two_pair,three,full,four,five]:
    wanted = []
    now = sort_cards(lists)
    for item in now:
        if item not in wanted:
            wanted.append(item)
    ans += wanted
print(ans)
print(bids)
for yep in range(1000):
    real_ans += int(bids[ans[yep]]) * (yep + 1)
print(real_ans)


