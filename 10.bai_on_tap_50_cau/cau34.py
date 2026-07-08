def remove_duplicates_nn(arr):
    res = []
    for x in arr:
        if x not in res:
            res.append(x)
    return res

def remove_duplicates_n(arr):
    seen = set()
    res = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            res.append(x)
    return res

print("Cách O(n^2):", remove_duplicates_nn([3, 1, 3, 2, 1]))
print("Cách O(n):", remove_duplicates_n([3, 1, 3, 2, 1]))