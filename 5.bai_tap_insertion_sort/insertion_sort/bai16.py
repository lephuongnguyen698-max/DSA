def sap_xep_truc_tuyen(stream):

    arr = []

    for value in stream:

        arr.append(value)

        i = len(arr) - 2

        while i >= 0 and arr[i] > value:
            arr[i + 1] = arr[i]
            i -= 1

        arr[i + 1] = value

        print(arr)


stream = [5, 2, 8, 1]

sap_xep_truc_tuyen(stream)