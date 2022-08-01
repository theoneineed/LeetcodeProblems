class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = 0
        l_sum = ListNode()
        head = l_sum
        
        while l1 or l2:
            sum_val = res + (l1.val if l1 != None else 0) + (l2.val if l2 != None else 0)
            head.val = sum_val % 10
            res = sum_val // 10
            
            if l1 != None: l1=l1.next 
            if l2 != None: l2=l2.next
            if (l1 or l2):
                head.next = ListNode()
                head = head.next
            elif res != 0:
                head.next = ListNode()
                head = head.next
                head.val = res
            else:
                continue
        return l_sum