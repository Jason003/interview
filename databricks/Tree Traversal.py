'''
Tree Traversal without recursion and without stack and without changing the Tree
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

'''
Let current store the currently visited node (initialized to the root of the tree)
Let source represent how we got to the current node. It's one of FROM_PARENT, FROM_LEFT_CHILD, FROM_RIGHT_CHILD. (Initialized to FROM_PARENT)
'''
def traverse(root):
    source = 'p'
    curr = root
    while curr:
        if source == 'p':
            print(curr.val)
            if curr.left:
                curr = curr.left
                source = 'p'
            else:
                source = 'l' # we pretend to have finished left part and come from left
        elif source == 'l': # we are going to visit right part
            if curr.right:
                curr = curr.right
                source = 'p'
            else:
                source = 'r' # we pretend to have finished the right part and come from right
        else: # after finishing right part, we are going back to parent
            if not curr.parent:
                return
            source = 'l' if curr == curr.parent.left else 'r'
            curr = curr.parent
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
one.left, one.right = two, three
two.parent, three.parent = one, one
three.right = four
four.parent = three
traverse(one)
