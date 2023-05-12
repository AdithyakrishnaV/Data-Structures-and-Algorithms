# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Check if either list is null
        if not list1:
            return list2
        if  not list1:
            return list2
        #declare and initil head
        head: Optional[ListNode] = ListNode(0)
        current: Optional[ListNode] = head
        while list1 and list2: #loop until the lists are empty

            if list1.val <= list2.val:
                current.next = list1 #small value comes first
                list1 = list1.next #changing the pointer function


            else:
                current.next = list2
                list2 = list2.next #changing the pointer function

            current = current.next # changing the current position to the newest inside the iteration

        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        return head.next