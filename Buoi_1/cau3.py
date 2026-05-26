def linearsearch(arr, key):

    for i in range(len(arr)):

        if arr[i] == key:

            return i

    return -1


arr = ['Bao','An','Dat','Duc','Hung','Phi','Vinh','Dung']

key = 'Phi'

print("phan tu tim thay duoc tai vi tri la: " + str(linearsearch(arr,key)))