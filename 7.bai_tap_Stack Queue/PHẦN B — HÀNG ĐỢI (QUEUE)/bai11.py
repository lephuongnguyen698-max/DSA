from collections import deque


def cua_so_lon_nhat(mang, k):

    hang_doi = deque()
    ket_qua = []

    for i in range(len(mang)):

        while (hang_doi and hang_doi[0] <= i - k):
            hang_doi.popleft()

        while (hang_doi and mang[hang_doi[-1]] < mang[i]):
            hang_doi.pop()

        hang_doi.append(i)

        if i >= k - 1:

            ket_qua.append(mang[hang_doi[0]])

    return ket_qua


a = [1, 3, -1, -3, 5, 3]

print(cua_so_lon_nhat(a, 3))