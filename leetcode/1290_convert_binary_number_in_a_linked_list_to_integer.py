# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ''

        while head is not None:
            s += str(head.val)
            head = head.next

        return int(s, 2)


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(0)
    c = ListNode(1)

    b.next = c
    a.next = b

    print(Solution().getDecimalValue(a))

    # print(int('101', 2))
