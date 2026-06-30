# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Get our heads
        ptr1 = list1
        ptr2 = list2
        merged  = None

        # Case: Lists missing
        if not ptr1:
            if not ptr2:
                return merged
            return ptr2

        if not ptr2:
            if not ptr1:
                return merged
            return ptr1

        # Create new head
        if(ptr1.val < ptr2.val):
            merged = ptr1
            ptr1 = ptr1.next
        else:
            merged = ptr2
            ptr2 = ptr2.next

        mergedHead =  merged

        # merge after head
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                merged.next = ptr1
                ptr1 = ptr1.next
                merged = merged.next
            else:
                merged.next = ptr2
                ptr2 = ptr2.next
                merged = merged.next
            
        # After completing merge, add any reminders
        if ptr1:
            merged.next = ptr1

        if ptr2:
            merged.next = ptr2
        
        return mergedHead



        