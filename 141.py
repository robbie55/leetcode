class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



nodeA = ListNode(3)
nodeB = ListNode(2)
nodeC = ListNode(0)
nodeD = ListNode(-4)
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeB


def hasCycle(head, pos):
    currentNode = head
    if currentNode.val == currentNode.next.val:
        return True
    linkedListLength = 0
    linkedList = []
    linkedList.append(currentNode.val)
    while True:
        prevNode = currentNode
        currentNode = currentNode.next
        if currentNode.val in linkedList:
            currentNode = prevNode
            break
        linkedList.append(currentNode.val)
        # if len(linkedList) != len(set(linkedList)):
        #     linkedList.pop()
        #     break
        linkedListLength += 1
    tail = prevNode
    
    for i in range(linkedListLength): 
        if tail.val == linkedList[pos]:
            return True
        tail = tail.next
    return False

print(hasCycle(nodeA, 0))
