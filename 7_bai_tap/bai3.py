class DoThi:
    def __init__(self):
        self.do_thi = {
            "A": [("B", 2), ("C", 5)],
            "B": [],
            "C": [("B", -4)]
        }

    def hien_thi(self):
        for dinh in self.do_thi:
            print(dinh, "->", self.do_thi[dinh])


do_thi = DoThi()

print("Đồ thị có cạnh âm:")
do_thi.hien_thi()

print("\nĐường đi trực tiếp A -> B =", 2)
print("Đường đi A -> C -> B =", 5 + (-4))
print("Kết quả đúng là 1.")
print("Dijkstra sẽ chọn 2 nên cho kết quả sai.")
print("Thuật toán thay thế: Bellman-Ford")