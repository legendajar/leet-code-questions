# program to add two linked list in reverse order
# in this we have given two linked list and then we have to add these two linked list and return it in reverse order


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumber(l1,l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total_sum = val1 + val2 + carry

        carry = total_sum // 10

        current.next = ListNode(total_sum % 10)

        current = current.next

        if l1:
            l1 = l1.next
        
        if l2:
            l2 = l2.next

        
    if carry > 0:
        current.next = ListNode(carry)
        
    return dummy.next



if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = addTwoNumber(l1, l2)

    while result:
        print(result.val, end=" ")
        result = result.next