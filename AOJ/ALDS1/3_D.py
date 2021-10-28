from collections import deque
from typing import Deque, List


class SolveCrossSectionDiagram:
    def __init__(self):
        self.depth_stack: Deque[int] = deque()
        self.area_stack: Deque[List[int]] = deque()

    def execute(self, diagram):
        for idx, s in enumerate(diagram):
            if s == '\\':
                self.depth_stack.append(idx)
            elif s == '/':
                if len(self.depth_stack) > 0:
                    top_idx = self.depth_stack.pop()
                    area = [top_idx, idx - top_idx]
                    while len(self.area_stack) > 0:  # 水たまりの結合
                        top_area = self.area_stack.pop()
                        if top_area[0] > top_idx:
                            area[1] += top_area[1]
                        else:
                            self.area_stack.append(top_area)
                            break
                    self.area_stack.append(area)

            elif s == '_':
                pass

        a = 0
        k = 0
        l = []
        for area in self.area_stack:
            a += area[1]
            k += 1
            l.append(str(area[1]))
        return a, k, l


def main():
    diagram = input()
    a, k, l = SolveCrossSectionDiagram().execute(diagram=diagram)
    print(a)
    print(f'{k}{" " + " ".join(l) if len(l) > 0 else ""}')


main()
