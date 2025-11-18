# Definition for singly-linked list.
from collections import deque

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode: 
        val1 = self.reverseNodeInDigits(l1)
        val2 = self.reverseNodeInDigits(l2)
        sum_val = val1 + val2
        return self.digitToLinkedList(sum_val)
    
    def reverseNodeInDigits(self, node: ListNode) -> int:
        lst = []
        while node:
            lst.insert(0, node.val)
            node = node.next
        return int("".join(map(str, lst)))

    def digitToLinkedList(self, digit: int) -> ListNode:
        array = self.reverseDigitToArray(digit)
        node = ListNode(array[0])
        current = node
        for i in array[1:]:
            current.next = ListNode(i)
            current = current.next
        return node

    def reverseDigitToArray(self, digit: int):
        return [int(x) for x in str(digit)][::-1]
        
####### local run ########################
'''
def printNode(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print("".join(values))

def run_case(solution, l1, l2, case_name=""):
    print(f"--- {case_name} ---")
    val1 = solution.reverseNodeInDigits(l1)
    val2 = solution.reverseNodeInDigits(l2)
    sum_val = val1 + val2
    print("sum:", sum_val)
    new_node = solution.digitToLinkedList(sum_val)
    printNode(new_node)

def main():
    solution = Solution()

    # Case 1
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    run_case(solution, l1, l2, "Case 1")

    # Case 2
    l1 = ListNode(0)
    l2 = ListNode(0)
    run_case(solution, l1, l2, "Case 2")

    # Case 3
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    run_case(solution, l1, l2, "Case 3")
    

if __name__=="__main__":
    main()
'''