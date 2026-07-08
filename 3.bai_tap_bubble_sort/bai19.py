def min_passes_needed(a):
    sorted_a = sorted(a)
    max_distance = 0

    for i in range(len(a)):
        correct_pos = sorted_a.index(a[i])

        if i - correct_pos > max_distance:
            max_distance = i - correct_pos

    return max_distance


a = [1, 2, 3, 5, 4]

print(min_passes_needed(a))