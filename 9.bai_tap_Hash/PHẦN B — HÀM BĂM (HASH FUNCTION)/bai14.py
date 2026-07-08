bit = [0] * 10

for x in ["a", "b"]:

    bit[hash(x) % 10] = 1

print(bit)

print("a:", bit[hash("a") % 10] == 1)