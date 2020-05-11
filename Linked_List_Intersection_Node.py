# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        runA = headA
        runB = headB

        lenA = 0
        while runA:
            lenA += 1
            runA = runA.next
        lenB = 0
        while runB:
            lenB += 1
            runB = runB.next

        runA = headA
        runB = headB

        if lenA > lenB:
            diffA = lenA - lenB
            while diffA:
                runA = runA.next
                diffA -= 1
        if lenB > lenA:
            diffB = lenB - lenA
            while diffB:
                runB = runB.next
                diffB -= 1
        while runA:
            if runA == runB:
                return runA
            runA = runA.next
            runB = runB.next

        return None


