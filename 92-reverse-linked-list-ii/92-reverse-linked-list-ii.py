# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if head == right :
            return head
        current_node=head
        counter=1
        nodes_list=[]
        while True:
            if counter>right:
                break
            if counter>=left:
                nodes_list.append(current_node.val)
            current_node=current_node.next
            counter+=1
        current_node=head
        counter=1
        while True:
            if counter>right:
                break
            if counter>=left :
                current_node.val=nodes_list.pop()
            current_node=current_node.next
            counter+=1
        return head