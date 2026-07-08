A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

giao = len(A & B)
hop = len(A | B)

print("Jaccard =", giao / hop)