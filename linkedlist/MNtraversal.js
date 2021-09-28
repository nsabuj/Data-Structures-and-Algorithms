

class ListNode {
    constructor(val, next = null) {
      this.val = val;
      this.next = next;
    }
  }
  // ---- Generate our linked list ----
  const linkedList = [8,7,6,5, 4, 3, 2, 1].reduce((acc, val) => new ListNode(val, acc), null);
  
  // ---- Generate our linked list ----
  
  const printList = (head) => {
    if(!head) {
      return;
    }
  
    console.log(head.val);
    printList(head.next);
  }
  
  // --------- Our solution -----------
  
  var reverseBetween = function(head, m, n) {
    let currentPos = 1, currentNode = head;
    let start = head;
    
    while(currentPos < m) {
      start = currentNode;
      currentNode = currentNode.next;
      currentPos++;
    }
    
    let newList = null, tail = currentNode;
   
    while(currentPos >= m && currentPos <= n) {
     // 2
      const next = currentNode.next; //3
      currentNode.next = newList; ///tail is null 
      newList = currentNode;      // creating a list reversing the nodes one by one
      currentNode = next;
      
      currentPos++;
    }
    
    start.next = newList;
    tail.next = currentNode;
    
    if(m > 1) {
      return head
    } else {
      return newList;
    }
  };
  
  printList(linkedList);
  console.log('after reverse');
  printList(reverseBetween(linkedList, 2, 7));
  