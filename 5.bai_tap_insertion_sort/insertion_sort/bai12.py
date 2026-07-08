def sap_xep_do_dai_chuoi(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and len(arr[j]) > len(key):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


arr = ['abc', 'a', 'ab']

print(sap_xep_do_dai_chuoi(arr))