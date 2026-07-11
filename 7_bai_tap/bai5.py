from collections import deque


def gia_tri_nho_nhat(ds, k):
    hang_doi = deque()
    ket_qua = []

    for i in range(len(ds)):

        while hang_doi and hang_doi[0] <= i - k:
            hang_doi.popleft()

        while hang_doi and ds[hang_doi[-1]] >= ds[i]:
            hang_doi.pop()

        hang_doi.append(i)

        if i >= k - 1:
            ket_qua.append(ds[hang_doi[0]])

    return ket_qua


ds = [4, 2, 12, 11, -5, 8, 1, 5, 6]
k = 3

print("Mảng:", ds)
print("Giá trị nhỏ nhất mỗi cửa sổ:", gia_tri_nho_nhat(ds, k))