class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        covered_path = set()
        while head:
            if head in covered_path:
                return True
            covered_path.add(head)
            head = head.next
        return False
    #if there is a cycle, the path covered is bound to be repeated which means, we will find the repeated head in the     #set
  