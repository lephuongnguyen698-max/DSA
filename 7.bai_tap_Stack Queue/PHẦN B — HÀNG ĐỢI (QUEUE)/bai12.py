from collections import deque


def josephus(n, k):
    hang_doi = deque()

    for i in range(1, n + 1):
        hang_doi.append(i)

    while len(hang_doi) > 1:

        for _ in range(k - 1):

            hang_doi.append(hang_doi.popleft())

        hang_doi.popleft()

    return hang_doi[0]


print(josephus(5, 2))