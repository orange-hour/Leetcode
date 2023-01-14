# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
       dummy = ListNode(0) #dummy head for the resulting list
       curr = dummy
       carry = 0
       while l1 != None or l2 != None or carry !=0:
           l1val = l1.val if l1 else 0
           l2val = l2.val if l2 else 0
           columnsum = l1val + l2val + carry
           carry = columnsum // 10
           newNode = ListNode(columnsum % 10)
           curr.next = newNode #set next node to newnode
           curr = newNode #advance current node to next
           l1 = l1.next if l1 else None #advance l1 if l1 exists
           l2 = l2.next if l2 else None
        return dummy.next #returns the first node of the resulting list
