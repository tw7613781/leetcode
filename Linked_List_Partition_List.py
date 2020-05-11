class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def PartitionList(self,head,x):
        # type head: Linked Node
        # type x: integer
        # rtype: ListNode
        L = ListNode(0)
        EG = ListNode(0)
        L.next = EG.next = head
        Lrun = L
        EGrun = EG
        run = head
        while run:
            if run.val < x:
                Lrun.next = run
                Lrun = Lrun.next
            else:
                EGrun.next = run
                EGrun = EGrun.next
            run = run.next
        if EG.next != head or L.next != head:
            Lrun.next = EG.next
            EGrun.next = None
        return L.next

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


s = [1,4,3,2,5,2]
s = [1,1,2,2]
s = [5,7,6,8]
s = [1]
s = []
s = [1,1,1,1]
s = [7,6,5,4,3,2,1]
solution = Solution()
head = solution.buildLinkedList(s)
solution.printLinkedList(head)
print('--------------------------')
head = solution.PartitionList(head,3)
solution.printLinkedList(head)
