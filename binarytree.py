class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert(self, value):
        self._insert_recursively(self.root, value)

    def _insert_recursively(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursively(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursively(current_node.right, value)

    def search(self, value):
        return self._search_recursively(self.root, value)

    def _search_recursively(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self._search_recursively(current_node.left, value)
        else:
            return self._search_recursively(current_node.right, value)
