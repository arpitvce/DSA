class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
       dummy=ListNode(-1)
       dummy.next=head
       leftnode=head
        for _ in range(1,left):
            leftnode=leftnode.next
        rightnode=head
        for _ in range(1,right):
            rightnode=rightnode.next
        temp=leftnode
        temp=temp.next
        leftnode.next=rightnode.next
        while temp!=rightnode:
            leftnode.next=temp
            temp=temp.next
            leftnode=leftnode.next
        return dummy.next
