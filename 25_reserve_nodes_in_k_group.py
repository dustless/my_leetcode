#Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __str__(self):
        s = "%s" % self.val
        tmp = self
        while tmp.next:
            tmp = tmp.next
            s += "->%s" % tmp.val
        return s


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if not head:
            return None
        list = [head]
        p = head
        for i in range(1, k):
            if not p.next:
                return head
            list.append(p)
            p = p.next

        head = p
        q = p.next

        for i in range(1, k):
            p.next = list.pop()
            p = p.next
        p.next = self.reverseKGroup(q, k)

        return head


if __name__ == "__main__":
    root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print Solution().reverseKGroup(root, 2)
