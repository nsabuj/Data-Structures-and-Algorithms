import random
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class Stack:
    def __init__(self):
        self.top=None
        self.size=0
        self.min=None

    def __str__(self):
        current=self.top
        output=""
        while current:
            output+=str(current.value)+'>'
            current=current.next
        return output[:-1]
    __repr__=__str__ 

    def __len__(self):
        current=self.top
        count=0
        while current:
            count+=1
            current=current.next
        return count
    def isEmpty(self):
        return self.size==0
    def peek(self):
        if self.top==None:
            return None
        else:
            if self.top.value<self.min:
                return "Top most element is {}".format(self.min)
            else:
                return "Top most element is {}".format(self.top.value)

    def push(self,value):
        
        if self.top==None:
            new_node=Node(value)
            self.top=new_node
            
            self.min=new_node.value
        elif value<self.min:
            
            temp=value*2-self.min
            new_node=Node(temp)
            self.min=value
            new_node.next=self.top
            self.top = new_node
        else:
            new_node=Node(value)
            new_node.next=self.top
            self.top = new_node                  
        self.size += 1
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        else:

            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.min:
                print ("Top Most Element Removed :{} " .format(self.min))
                self.min = ( ( 2 * self.min) - removedNode )
            else:
                print ("Top Most Element Removed : {}" .format(removedNode))
            self.size-=1    

# Driver Code
if __name__ == "__main__":
   stack = Stack()
   arr=[10,120,126,200,123,12,134,10,19,40,0]
   for i in range(len(arr)):
      stack.push(arr[i])
   print(f"Stack: {stack}") 
   print(stack.size)
   print("minimum value in the stack {}".format(stack.min))
   stack.pop()
   print(f"Stack: {stack}")        
   stack.pop()
   print(f"Stack: {stack}")
   print("minimum value in the stack {}".format(stack.min))

