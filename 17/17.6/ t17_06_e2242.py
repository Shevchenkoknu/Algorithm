n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None

    def Insert(self, val):
        self.head = self._insert_recursive(self.head, val)

    def _insert_recursive(self, node, val):
        if node is None:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        else:
            node.right = self._insert_recursive(node.right, val)
        return node

    def SameTree(self, other_tree):
        return 1 if self._same_tree(self.head, other_tree.head) else 0

    def _same_tree(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return (node1.val == node2.val and
                self._same_tree(node1.left, node2.left) and
                self._same_tree(node1.right, node2.right))

tree1 = Tree()
for val in arr1:
    tree1.Insert(val)

tree2 = Tree()
for val in arr2:
    tree2.Insert(val)

print(tree1.SameTree(tree2))
