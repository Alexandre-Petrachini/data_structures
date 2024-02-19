from typing import Optional, List

class TreeNode:
    """Represents a node in a binary tree."""

    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Tree:
    """Implements a binary tree with insertion and deletion operations."""

    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None

    def insert(self, key: int) -> Optional[TreeNode]:
        """
        Inserts a new key into the tree using level order traversal.

        Args:
            key (int): The value to insert into the tree.

        Returns:
            TreeNode: The root of the tree after insertion.
        """
        if not self.root:
            self.root = TreeNode(key)
            return self.root

        q: List[TreeNode] = [self.root]
        while q:
            temp = q.pop(0)
            if not temp.left:
                temp.left = TreeNode(key)
                break
            q.append(temp.left)

            if not temp.right:
                temp.right = TreeNode(key)
                break
            q.append(temp.right)
        return self.root

    def delete(self, key: int) -> Optional[TreeNode]:
        """
        Deletes a node with the specified key from the tree.

        Args:
            key (int): The value of the node to delete.

        Returns:
            TreeNode: The root of the tree after deletion.
        """
        if not self.root:
            return None

        del_node = None
        q = [self.root]

        while q:
            temp = q.pop(0)
            if temp.val == key:
                del_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

        if del_node:
            x = temp.val
            self.delete_deepest(temp)
            del_node.val = x
        return self.root

    def delete_deepest(self, d_node: TreeNode) -> None:
        """
        Deletes the deepest rightmost node in the tree.

        Args:
            d_node (TreeNode): The node to delete.
        """
        q = [self.root]
        while q:
            temp = q.pop(0)
            if temp is d_node:
                temp = None
                return
            if temp.right:
                if temp.right is d_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left is d_node:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)

    def print_inorder(self, node: Optional[TreeNode]) -> None:
        """
        Prints the nodes of the tree in an inorder traversal.

        Args:
            node (TreeNode): The current node to process.
        """
        if node:
            self.print_inorder(node.left)
            print(node.val, end=' ')
            self.print_inorder(node.right)

    def is_bst(self) -> bool:
        """
        Checks if the tree is a binary search tree (BST).

        Returns:
            bool: True if the tree is a BST, False otherwise.
        """
        def is_bst_util(node: Optional[TreeNode], left: int, right: int) -> bool:
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return (is_bst_util(node.left, left, node.val) and
                    is_bst_util(node.right, node.val, right))

        return is_bst_util(self.root, float('-inf'), float('inf'))