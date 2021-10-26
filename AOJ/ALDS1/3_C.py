from collections import deque


class Deque:
    def __init__(self):
        self.nil: Node = Node()

    def insert_first(self, data):
        new_node = Node(data=data)
        self.nil.next.prev = new_node
        new_node.next = self.nil.next
        new_node.prev = self.nil
        self.nil.next = new_node

    def delete_first(self):
        first_node = self.nil.next
        self.nil.next = first_node.next
        first_node.next.prev = self.nil

    def delete_last(self):
        last_node = self.nil.prev
        self.nil.prev = last_node.prev
        last_node.prev.next = self.nil

    def delete_data(self, data):
        node = self.nil.next
        while True:
            if node.data == data:
                self._delete_node(node=node)
                break
            if node.data is None:
                break
            node = node.next

    def _delete_node(self, node: 'Node'):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get_all(self):
        node = self.nil.next
        result = []
        while node.data is not None:
            result.append(node.data)
            node = node.next
        return result


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: 'Node' = self
        self.prev: 'Node' = self


def main():
    dq = deque()
    n = int(input())
    for i in range(n):
        _input = input()
        if _input == 'deleteFirst':
            dq.popleft()
        elif _input == 'deleteLast':
            dq.pop()
        else:
            command, data = _input.split()
            if command == 'insert':
                dq.appendleft(data)
            elif command == 'delete':
                try:
                    dq.remove(data)
                except:
                    pass
            else:
                raise Exception(f'wrong command {command}')

    print(' '.join(dq))


main()
