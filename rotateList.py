# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        
        node = head
        length = 0
        
        while node:
            node = node.next
            length += 1
            
        rotate_in = length - k % length
        
        if rotate_in == length:
            return head
        
        node = head
        
        for i in range(rotate_in -1):
            node = node.next
            
        temp = node.next
        
        node.next = None
        temp2 = temp
        
        while temp2 and temp2.next:
            temp2 = temp2.next
        temp2.next = head
        return temp
    