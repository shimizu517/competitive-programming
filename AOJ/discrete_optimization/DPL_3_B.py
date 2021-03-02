from collections import deque
from typing import Deque

H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(H)]


class Rect:
    def __init__(self, height, pos):
        self.height = height
        self.pos = pos


def getLargestRectangleAreaInHistogram(hist):
    max_area = 0
    hist_end_with_zero = hist + [0]
    stack: Deque[Rect] = deque()
    for i, rect_h in enumerate(hist_end_with_zero):
        # stackが空の時
        if not stack or stack[-1].height < rect_h:
            stack.append(Rect(height=rect_h, pos=i))
        elif stack[-1].height > rect_h:
            top = Rect(0, 0)
            while stack and stack[-1].height > rect_h:
                top = stack.pop()
                max_area = max((i - top.pos) * top.height, max_area)
            stack.append(Rect(height=rect_h, pos=top.pos))

    return max_area


def solve():
    histograms = [[0] * W for _ in range(H)]
    for i in range(W):
        histograms[0][i] = int(c[0][i] == 0)
    for i in range(1, H):
        for j in range(W):
            if c[i][j] == 1:
                histograms[i][j] = 0
            else:
                histograms[i][j] = histograms[i - 1][j] + 1

    result = 0
    for hist in histograms:
        result = max(result, getLargestRectangleAreaInHistogram(hist=hist))

    return result


print(solve())
