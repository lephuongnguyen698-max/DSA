def tao_do_thi():

    adj = [
        [(1, 4), (2, 1)],
        [(3, 1)],
        [(1, 2), (3, 5), (4, 8)],
        [(4, 3), (5, 6)],
        [(5, 2)],
        []
    ]

    return adj


def in_danh_sach_ke(adj):

    for i in range(len(adj)):
        print(f"adj[{i}] = {adj[i]}")


graph = tao_do_thi()

in_danh_sach_ke(graph)