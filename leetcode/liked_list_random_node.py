import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head):
        self.head = head
    def getRandom(self):
        n, k = 1, 1
        head, ans = self.head, self.head
        while head.next:
            n += 1
            head = head.next
            if random.random() < k/n:
                ans = ans.next
                k += 1
        return ans.val


item1 = ListNode(1)
item2 = ListNode(2, item1)
item3 = ListNode(3, item2)

sol = Solution(item3)
print(sol.getRandom())