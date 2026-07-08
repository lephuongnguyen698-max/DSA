from collections import deque


def round_robin(cong_viec, quantum):

    hang_doi = deque(cong_viec)
    thoi_gian = 0

    while hang_doi:
        ten, tg = hang_doi.popleft()

        if tg <= quantum:
            thoi_gian += tg

            print(ten, "xong lúc", thoi_gian)

        else:
            thoi_gian += quantum
            hang_doi.append((ten, tg - quantum))


cong_viec = [
    ("P1", 5),
    ("P2", 3),
    ("P3", 1)
]

round_robin(cong_viec, 2)