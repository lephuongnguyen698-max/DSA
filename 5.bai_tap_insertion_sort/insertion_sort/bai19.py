def gnome_sort(arr):

    index = 0

    while index < len(arr):

        if index == 0:
            index += 1

        elif arr[index] >= arr[index - 1]:
            index += 1

        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1

    return arr


arr = [3, 2, 1]

print(gnome_sort(arr))