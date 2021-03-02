from collections import deque
from typing import Deque


class Rect:
    def __init__(self, height, pos):
        self.height = height
        self.pos = pos


def solve(h: [int]):
    stack: Deque[Rect] = deque()
    histogram = h + [0]
    max_area = 0
    for idx, height in enumerate(histogram):
        if not stack or stack[-1].height < height:
            stack.append(Rect(height=height, pos=idx))
        elif stack[-1].height > height:
            # while文の後にstackにpushする長方形のposのためにここでtopを宣言する
            # 実際whileは100%実行されるが、コードの解析でワーニングが出るため、topを宣言している
            top = Rect(height=0, pos=0)
            while stack and stack[-1].height > height:
                top = stack.pop()
                max_area = max(max_area, (idx - top.pos) * top.height)
            stack.append(Rect(height=height, pos=top.pos))

    return max_area


def main():
    N = int(input())
    h = list(map(int, input().split()))
    print(solve(h=h))


main()
