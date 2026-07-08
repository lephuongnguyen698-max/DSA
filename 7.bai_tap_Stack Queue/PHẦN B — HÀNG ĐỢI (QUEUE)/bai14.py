from collections import deque


class DemHit:

    def __init__(self):
        self.hang_doi = deque()

    def them_hit(self, thoi_gian):
        self.hang_doi.append(thoi_gian)

    def dem(self, hien_tai):

        while (self.hang_doi and self.hang_doi[0] <= hien_tai - 300):

            self.hang_doi.popleft()

        return len(self.hang_doi)


bo_dem = DemHit()

bo_dem.them_hit(1)
bo_dem.them_hit(100)
bo_dem.them_hit(300)

print(bo_dem.dem(301))