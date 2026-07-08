def max_rectangle_histogram(heights):
    stack = []
    max_area = 0
    n = len(heights)
    
    for i in range(n):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
        
    while stack:
        h = heights[stack.pop()]
        w = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, h * w)
        
    return max_area

print(max_rectangle_histogram([2, 1, 5, 6, 2, 3]))