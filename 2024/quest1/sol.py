from collections import Counter

with open("./everybody_codes_e2024_q1_p1.txt") as f:
    p1 = f.read()
counts = Counter(p1)
print(counts["B"] + counts["C"] * 3)

with open("./everybody_codes_e2024_q1_p2.txt") as f:
    p2 = f.read()

scores = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}


def pairscore(pair, scores=scores):
    if pair[0] == "x":
        return scores[pair[1]]
    if pair[1] == "x":
        return scores[pair[0]]
    return sum([scores[i] + 1 for i in pair])


assert len(p2) % 2 == 0
print(sum([pairscore(p2[i : i + 2]) for i in range(0, len(p2), 2)]))

with open("./everybody_codes_e2024_q1_p3.txt") as f:
    p3 = f.read()


def tripscore(pair, scores=scores):
    if pair[0] == "x":
        return pairscore(pair[1:])
    elif pair[1] == "x":
        return pairscore(pair[0] + pair[2])
    elif pair[2] == "x":
        return pairscore(pair[:2])
    return sum([scores[i] + 2 for i in pair])


assert len(p3) % 3 == 0
print(sum([tripscore(p3[i : i + 3]) for i in range(0, len(p3), 3)]))
