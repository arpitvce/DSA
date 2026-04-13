class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(-1)
        dummy.next=head
        start=dummy.next
        for _ in range(1,left):
            start=start.next
        end=dummy.next
        temp=dummy.next
        temp=start.next
        for _ in range(1,right):
            end=end.next
        curr=start
        start.next=end.next
        nxt=None
        while (nxt!=end):
            nxt=temp.next
            temp.next=curr
            curr=temp
            temp=nxt
        return dummy.next
