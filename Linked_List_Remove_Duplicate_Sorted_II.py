class ListNode:
    def __init__(self,x):
        self.value = x
        self.next = None

class Solution:
    def RemoveDuplicates(self,head):
        # type head: Linked Node
        # rtype: ListNode
        if head == None:
            return head
        d= {}
        run = head
        while(run != None):
            val = run.value
            if d.get(val):
                d[val] += 1
            else:
                d[val] = 1
            run = run.next
        val = head.value
        while  d[val] > 1:
            head = head.next
            if head == None:
                return head
            val = head.value
        run = head
        while run and run.next:
            subRun = run
            while subRun.next is not None and d[subRun.next.value] > 1:
                subRun = subRun.next
            run.next = subRun.next
            run = run.next
        print(d)
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
            print(run.value)
            run = run.next


s = [1,2,2,3,3]
# s = [1,2,3]
# s = [2,2]
# s = [2]
# s = [1,1,2]
s = []
s = [1]
s = [1,1]
s = [1,1,2]
s = [1,1,2,2,3,3,4,5]
s = [1,2,3,4,5,6,6,6,7]
s = [1,2,2]
solution = Solution()
head = solution.buildLinkedList(s)
solution.printLinkedList(head)
print('--------------------------')
head = solution.RemoveDuplicates(head)
solution.printLinkedList(head)
