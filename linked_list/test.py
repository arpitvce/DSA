from reverse_entire_linked_list import ListNode,Solution
from typing import Optional
from rich import print
from rich.console import Console
import time

console=Console()
def build_ll(arr:list)->Optional[ListNode]:
    if not arr:
        return None
    head=ListNode(arr[0])
    actual_head=head
    for i in arr[1:]:
        temp=ListNode(i)
        head.next=temp
        head=head.next
    return actual_head

def print_ll(head:Optional[ListNode])->None:
    while head.next!=None:
        print(f"[yellow]{head.val}[/yellow] [bold red]->[/bold red]",end="")
        head=head.next
    print(f"[yellow]{head.val}[/yellow]")
    print()
    return None

arr=[1,2,3,4,5,6,7]

head=build_ll(arr)
print("[bold Green]Input: [/bold Green]")
print_ll(head)

with console.status("[bold cyan]Reversing your Linked List......[/bold cyan]",spinner="dots"):
    time.sleep(3)
    new_head=Solution().reverseList(head)
print("[bold red]Output:[/bold red]")
print_ll(new_head)

