import math

def min_eating_speed(piles, h):
    # Hàm kiểm tra xem tốc độ speed có ăn kịp trong h giờ không
    def can_eat_all(speed):
        hours_needed = 0
        for pile in piles:
            hours_needed += math.ceil(pile / speed)
        return hours_needed <= h

    left = 1
    right = max(piles)
    ans = right

    while left <= right:
        mid = (left + right) // 2
        if can_eat_all(mid):
            ans = mid          # Lưu lại tốc độ khả thi
            right = mid - 1    # Thử tìm tốc độ nhỏ hơn
        else:
            left = mid + 1     # Ăn không kịp, phải tăng tốc độ lên
    return ans

# Ví dụ
piles = [3, 6, 7, 11]
h = 8
print(f"Tốc độ nhỏ nhất: {min_eating_speed(piles, h)}")  # Output: 4