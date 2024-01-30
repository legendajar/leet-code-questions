# program to add two linked list in reverse order
# in this we have given two linked list and then we have to add these two linked list and return it in reverse order

'''
To solve this problem, you can follow these steps:

1. Initialize a dummy head node for the result linked list and a current node to keep track of the current position.
2. Initialize carry as 0, which will store the carry generated by adding two digits.
3. Traverse both input linked lists simultaneously until both of them reach the end.
4. At each iteration, add the values of the current nodes of both input linked lists along with the carry.
5. Calculate the sum and update the carry accordingly.
6. Create a new node with the value being the sum modulo 10 (to get the digit) and attach it to the result linked list.
7. Update the current node to the next position in the result linked list.
8. If one of the input linked lists has reached the end, continue adding digits from the other linked list along with the carry until both lists are exhausted.
9. Finally, if there is still a carry left after traversing both input linked lists, create a new node with the carry and append it to the result linked list.
10. Return the next node of the dummy head, which will be the head of the resulting linked list.
'''


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


