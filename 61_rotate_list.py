# Definition for singly-linked list.
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


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = self.lenOfList(head)
        if length <= 1:
            return head
        k = k % length
        if k == 0:
            return head
        return self.rotateLeft(head, length - k)

    def lenOfList(self, head):
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        return length

    def rotateLeft(self, head, k):
        if k == 0:
            return head

        p = head
        for i in range(0, k - 1):
            p = p.next
        new_head = p.next
        p.next = None

        q = new_head
        while q.next:
            q = q.next
        q.next = head
        return new_head


root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print Solution().rotateRight(root, 2)