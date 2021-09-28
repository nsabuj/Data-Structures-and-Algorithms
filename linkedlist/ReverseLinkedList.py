# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=None



class Solution:

    def __init__(self):
        self.head = None

    def reverseList(self):
        prev=None
        current=self.head
        while current:
            nxt=current.next
            current.next=prev
            prev=current
            current=nxt
            
        self.head= prev 


    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node   

    def printList(self):
        temp = self.head
        while(temp):
            print (temp.val)
            temp = temp.next         
#[1,2,3,4,5]
llist = Solution()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
 
print ("Given Linked List")
llist.printList()
llist.reverseList()
print ("\nReversed Linked List")
llist.printList()


        