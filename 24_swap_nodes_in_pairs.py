import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
parser.add_argument('--target', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    


list1 = list(args.input)
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
def swapPairs(self, head: ListNode) -> ListNode:
        
  dummy = temp = ListNode(0)
  
  if head:
    if head.next == None:
      return head
    dummy.next = head
    dummy.next.next = head
    while head.next.next:
      temp = head.next.next
      head.next.next = head
      head.next = temp
      
      head = head.next.next
        
    return dummy.next
  else:
    return []
        
 

print (swapPairs(0, list1))
