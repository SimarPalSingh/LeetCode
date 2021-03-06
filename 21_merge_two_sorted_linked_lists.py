import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='File path to CSV file with XPaths and values.')
parser.add_argument('--target', help='File path to CSV file with XPaths and values.')
args = parser.parse_args()    


list1 = args.input
list1 = "()"
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
  dummy = head = ListNode(0)
  while l1 and l2:
    if l1.val > l2.val:
      head.next = l2
      l2 = l2.next
    else:
      head.next = l1
      l1 = l1.next
    head = head.next
      
  if l1:
    head.next = l1
  if l2:
    head.next = l2
      
  return dummy.next

print (mergeTwoLists(0, list1))
