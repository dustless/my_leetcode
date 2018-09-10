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
    # @param a list of ListNode
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l = ListNode(l1.val)
            l1 = l1.next
        else:
            l = ListNode(l2.val)
            l2 = l2.next

        head = l
        while l1 and l2:
            if l1.val < l2.val:
                l.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l.next = ListNode(l2.val)
                l2 = l2.next
            l = l.next
        if not l1:
            l.next = l2
        elif not l2:
            l.next = l1

        return head

    def merge(self, lists, begin, end):
        if begin == end:
            return lists[begin]
        elif begin > end:
            return None

        mid = (begin + end) / 2
        left = self.merge(lists, begin, mid)
        right = self.merge(lists, mid + 1, end)

        return self.mergeTwoLists(left, right)

    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]

        return self.merge(lists, 0, len(lists) - 1)


if __name__ == "__main__":
    lists = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6)),
    ]
    print Solution().mergeKLists(lists)
