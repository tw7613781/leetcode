class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle2(self,head):
        # type head: ListNode
        # rtype: bool
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:
            return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head

    def buildLinkedList(self,s):
        # type s: integer array
        # rtype: ListNode
        if len(s) == 0:
            return None
        i = 1
        head = ListNode(s[0])
        run = head
        while i < len(s):
            node = ListNode(s[i])
            run.next = node
            run = node
            i += 1
        return head

    def printLinkedList(self,head):
        # type head: ListNode
        # rtype: None
        run = head
        while run != None:
            print(run.val)
            run = run.next


s= []
solution = Solution()
s = solution.buildLinkedList(s)
print(solution.hasCycle2(s))
