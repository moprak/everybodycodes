import re
from functools import reduce

import numpy as np

with open("./everybody_codes_e2024_q2_p1.txt") as f:
    d = f.read()
data = d.split("\n\n")
words = data[0][6:].split(",")
text = data[1]
print(sum(len(re.findall(w, text)) for w in words))

with open("./everybody_codes_e2024_q2_p2.txt") as f:
    d = f.read()
data = d.split("\n")
words = data[0][6:].split(",")
for w in words.copy():
    if w != w[::-1]:
        words.append(w[::-1])

res = 0
for text in data[2:]:
    found = np.zeros(len(text), dtype=int)
    for i in range(len(text)):
        for w in words:
            if text[i:].startswith(w):
                found[i : i + len(w)] = 1
    res += sum(found)
print(res)

with open("./everybody_codes_e2024_q2_p3.txt") as f:
    d = f.read()
data = d.split("\n")
words = data[0][6:].split(",")
text = data[2:]
for w in words.copy():
    if w != w[::-1]:
        words.append(w[::-1])

found = np.zeros((len(text), len(text[0])), dtype=int)
maxw = max(len(w) for w in words)
for j, s in enumerate(text):
    s_extend = s + s[:maxw]
    for i in range(len(s)):
        for w in words:
            if s_extend[i:].startswith(w):
                found[j, i : i + len(w)] = 1
                if i + len(w) > len(s):
                    found[j, : (i + len(w)) % len(s)] = 1
for j in range(len(text[0])):
    s = "".join(text[i][j] for i in range(len(text)))
    for i in range(len(s)):
        for w in words:
            if s[i:].startswith(w):
                found[i : i + len(w), j] = 1
print(found.sum())
