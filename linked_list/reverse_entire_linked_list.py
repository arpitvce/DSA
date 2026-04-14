from typing import Optional
class ListNode:
    def __init__(self,value=0,next=None):
        self.val=value
        self.next=None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        end=None
        temp=ListNode(-1)
        temp=head
        curr=temp
        while temp!=None:
            curr=temp.next
            temp.next=dummy.next
            dummy.next=temp
            temp=curr
        return dummy.next
