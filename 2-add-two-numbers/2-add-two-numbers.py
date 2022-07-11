# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current_node=l1
        current_digit=1
        l1_count=0
        while current_node:
            l1_count+=(current_node.val*current_digit)
            current_node=current_node.next
            current_digit*=10
        current_node=l2
        current_digit=1
        while current_node:
            l1_count+= (current_node.val*current_digit)
            current_node=current_node.next
            current_digit*=10
        current_digit=10
        l1=ListNode(l1_count%current_digit)
        l1_count=l1_count//current_digit
        l2=l1
        while l1_count:
            
            l2.next=ListNode(l1_count%current_digit)
            l2=l2.next
            l1_count=l1_count//current_digit
        return l1
    