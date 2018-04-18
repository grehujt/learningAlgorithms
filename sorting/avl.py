class Node(object):
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0


class AVL_Tree(object):
    root = None

    def _calc_height(self, node):
        if node is None:
            return -1
        else:
            return max(
                node.left.height if node.left else -1,
                node.right.height if node.right else -1) + 1

    def _left_rotation(self, node):
        if node.right:
            parent = node.parent
            node2 = node.right
            node.right = node2.left
            if node2.left: node2.left.parent = node
            node.parent = node2
            node2.left = node
            node2.parent = parent
            if parent:
                if parent.left is node: parent.left = node2
                else: parent.right = node2
            node.height = self._calc_height(node)
            node2.height = self._calc_height(node2)

    def _right_rotate(self, node):
        if node.left:
            parent = node.parent
            node2 = node.left
            node.left = node2.right
            if node2.right: node2.right.parent = node
            node.parent = node2
            node2.right = node
            node2.parent = parent
            if parent:
                if parent.left is node: parent.left = node2
                else: parent.right = node2
            node.height = self._calc_height(node)
            node2.height = self._calc_height(node2)

    def _rebalance(self, node):
        while node:
            self.root = node
            node.height = self._calc_height(node)
            if self._calc_height(node.left) > 1 + self._calc_height(node.right):
                if self._calc_height(node.left.left) >= self._calc_height(node.left.right):
                    self._right_rotate(node)
                else:
                    self._left_rotation(node.left)
                    self._right_rotate(node)
            elif self._calc_height(node.right) > 1 + self._calc_height(node.left):
                if self._calc_height(node.right.right) >= self._calc_height(node.right.left):
                    self._left_rotation(node)
                else:
                    self._right_rotate(node.right)
                    self._left_rotation(node)
            node = node.parent

    def _insert(self, root, node, parent):
        if root is None:
            node.parent = parent
            return node
        if node.key < root.key:
            root.left = self._insert(root.left, node, root)
        else:
            root.right = self._insert(root.right, node, root)
        root.height = self._calc_height(root)
        return root

    def _delete(self, root, key):
        # TODO
        pass


    def insert(self, key):
        node = Node(key)
        self._insert(self.root, node, None)
        self._rebalance(node)

    def delete(self, key):
        # TODO
        pass

    def build_tree(self, arr):
        self.root = Node(arr[0])
        for i in arr[1:]:
            self.insert(i)


def in_order_traverse(root):
    if root is None:
        return
    in_order_traverse(root.left)
    print(
        "key:", root.key,
        "left:", root.left.key if root.left else "none",
        "right:", root.right.key if root.right else "none",
        "parent:", root.parent.key if root.parent else "none",
        "height:", root.height)
    in_order_traverse(root.right)


avl = AVL_Tree()
avl.build_tree([3, 4, 5])
in_order_traverse(avl.root)
print('\n')
avl.insert(6)
in_order_traverse(avl.root)
print('\n')
avl.insert(7)
in_order_traverse(avl.root)
