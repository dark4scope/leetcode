from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head.next

        # 必须保证fast指针的值比slow位置靠前
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        mid = slow.next
        slow.next = None
        
        left, right = self.sortList(head), self.sortList(mid)

        res = ListNode(-1)
        h = res
        while left and right:
            if left.val<right.val:
                h.next = left
                left = left.next
            else:
                h.next =right
                right = right.next
            h = h.next
        if left:
            h.next = left
        else:
            h.next = right
        
        return res.next