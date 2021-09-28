from collections import deque


class RPN:
    def __init__(self):
        self.stack = deque()

    def execute(self, token):
        if token in ('+', '-', '*'):
            o1 = self.stack.pop()
            o2 = self.stack.pop()
            self.stack.append(self._calculate(o1, o2, token))
        else:
            self.stack.append(int(token))

    def _calculate(self, o1, o2, operator):
        if operator == '+':
            return o1 + o2
        elif operator == '-':
            return o2 - o1
        elif operator == '*':
            return o1 * o2
        else:
            raise Exception()

    def get_result(self):
        if len(self.stack) > 1:
            raise Exception()
        return self.stack.pop()


def main():
    input_list = list(map(str, input().split()))
    rpn = RPN()
    for item in input_list:
        rpn.execute(token=item)
    print(rpn.get_result())


main()
