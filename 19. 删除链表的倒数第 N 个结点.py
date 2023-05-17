class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur = head 
        for _ in range(1,n):
            if cur == None:
                return head
            else:
                cur = cur.next
        
        pre = ListNode(0)
        pre.next = head
        ans = pre
        while cur.next != None:
            ans = ans.next
            cur = cur.next
        
        del_note = ans.next
        ans.next = ans.next.next
        del(del_note)

        return pre.next
