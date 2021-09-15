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
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
  dummy = fast = slow = ListNode(0, next = head)
  
  for _ in range(n):
    fast = fast.next
      
  while fast.next:
    fast = fast.next
    slow = slow.next
  
  slow.next = slow.next.next
  
  return dummy.next