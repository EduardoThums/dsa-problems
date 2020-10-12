class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous_node = None
        current_node = head
        
        while current_node is not None:
            future_current_node = current_node.next
            
            current_node.next = previous_node
            previous_node = current_node
            
            current_node = future_current_node
        
        return previous_node
