# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not (head and head.next):
            return head
        rev = None
        if head.next.next:
            hold = head.next.next
            rev = self.swapPairs(hold)

        head2 = head.next
        head1 = head
        head2.next = head1
        head1.next = rev
        return head2