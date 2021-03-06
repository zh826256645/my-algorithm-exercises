# -*- encoding: utf-8 -*-
"""
自平衡二叉搜索树

由于二叉树搜索树不是严格的 O(logN), 因此在实际场景中没有用武之地

将数据导入二叉树后希望以“完全二叉树”的形式展示，才能做到查找是严格的 O(logN)
@File    :   AVL_tree.py
@Time    :   2020/08/28 11:12:57
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   None
"""
from model.binary_tree import BiTNode, BinarySearchTree
from utils.time import measure


class AVLNode(BiTNode):
    """AVL 节点
    比普通的二叉树节点多了一个高度值

    Args:
        BiTNode (): 二叉树节点
    """

    def __init__(self, element=None, left=None, right=None) -> None:
        super().__init__(element, left, right)
        self.height = 1


class AVLTree(BinarySearchTree):
    """AVL 树
    是最早被发明的平衡二叉树，又被称为高度平衡树
    查找、插入、删除平均和最坏情况下均是 O(logN)

    定义
    父节点的左子树和右子树的高度差不能大于 1，否则树就失去平衡，此时需要旋转节点

    Args:
        BinarySearchTree (): 二叉搜索树
    """

    def __init__(self, root: AVLNode = None) -> None:
        super().__init__(root)

    def rotate_right(self, root: AVLNode) -> AVLNode:
        """根节点的左子树的左节点失衡（单次右旋）

               [7]                  [5]
              /   \                /   \
            [5]   [8]  右旋       [4]   [7]
           /   \       --->     /     /   \
         [4]   [6]            [3]   [6]   [8]
         /
       [3]

        步骤：
        1.将根结点的左节点变为根结点
        2.新根节点的右节点变为原根结点的左节点
        3.原根结点变为新根结点的右节点

        Args:
            root (AVLNode): 根结点

        Returns:
            AVLNode: 新的根结点
        """
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        new_root.height = self.height(new_root)
        root.height = self.height(root)

        return new_root

    def rotate_left(self, root: AVLNode) -> AVLNode:
        """根结点的右子树的右节点失衡（单次左旋）

           [4]                     [6]
          /   \                   /   \
        [3]   [6]       左旋     [4]   [7]
             /   \      --->   /   \     \
           [5]   [7]          [3]   [5]   [8]
                    \
                    [8]

        步骤：
        1.将根结点的右节点变为根结点
        2.新根节点的左节点变为原根结点的右节点
        3.原根结点变为新根节点的左节点

        Args:
            root (AVLNode): 根结点

        Returns:
            AVLNode: 新的根结点
        """
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        new_root.height = self.height(new_root)
        root.height = self.height(root)

        return new_root

    def rotate_left_right(self, root: AVLNode) -> AVLNode:
        """根结点的左子树的右节点失衡（双旋转）

               [8]                 [8]                   [6]
              /   \               /   \                 /   \
            [5]   [9]   左旋     [6]   [9]   右旋       [5]   [8]
           /   \        --->   /   \        --->      /     /   \
         [4]   [6]           [5]   [7]             [4]   [7]   [9]
                  \         /
                   [7]    [4]

        步骤
        1.将根结点的左子树进行左旋
        2.将根结点进行右旋

        Args:
            root (AVLNode): 根结点

        Returns:
            AVLNode: 新的根结点
        """
        root.left = self.rotate_left(root.left)
        return self.rotate_right(root)

    def rotate_right_left(self, root: AVLNode) -> AVLNode:
        """根结点的右子树的左节点失衡（双旋转）

           [3]                   [3]                        [5]
          /   \                 /   \                      /   \
        [2]   [6]     右旋     [2]   [5]      左旋        [3]   [6]
             /   \    --->         /   \     --->       /   \     \
           [5]   [7]             [4]   [6]            [2]  [4]    [7]
           /                              \
         [4]                              [7]

        步骤
        1.将根结点的右子树进行右旋
        2.将根结点进行左旋

        Args:
            root (AVLNode): 根结点

        Returns:
            AVLNode: 新的根结点
        """

        root.right = self.rotate_right(root.right)
        return self.rotate_left(root)

    def put(self, element):
        """插入节点

        Args:
            element ([type]): [description]
        """
        new_node = AVLNode(element)
        new_root = self._put(new_node, self.root)

        self.root = new_root

    def _put(self, node: AVLNode, root: AVLNode) -> AVLNode:
        if not root:
            return node

        if node < root:
            root.left = self._put(node, root.left)
            if self.balance_factor(root.left, root.right) == 2:
                if node < root.left:
                    root = self.rotate_right(root)
                else:
                    root = self.rotate_left_right(root)

        else:
            root.right = self._put(node, root.right)
            if self.balance_factor(root.right, root.left) == 2:

                if node < root.right:
                    root = self.rotate_right_left(root)
                else:
                    root = self.rotate_left(root)

        root.height = self.height(root)

        return root

    def remove(self, node: AVLNode, key) -> AVLNode:
        """移除节点

        Args:
            node (AVLNode): 当前节点
            key ([type]): 移除的节点的 key

        Returns:
            AVLNode: 新的头节点
        """
        if not node:
            node = self.root
            self.root = self._remove(node, key)
        else:
            self._remove(node, key)

    def _remove(self, root: AVLNode, key) -> AVLNode:
        """移除节点

        Args:
            root (AVLNode): 根结点
            key ([type]): 移除节点的 key

        Returns:
            AVLNode: 新的根节点
        """
        if not root:
            return None

        if root.element > key:
            root.left = self._remove(root.left, key)
            if self.balance_factor(root.left, root.right) == 2:
                if root.left.element < key:
                    root = self.rotate_right(root)
                else:
                    root = self.rotate_left_right(root)

        elif root.element < key:
            root.right = self._remove(root.right, key)
            if self.balance_factor(root.left, root.right) == 2:
                if root.right.element > key:
                    root = self.rotate_left(root)
                else:
                    root = self.rotate_right_left(root)

        else:
            if not root.left and not root.right:
                return None
            elif root.right:
                root.element = self.successor(root)
                root.right = self._remove(root.right, root.element)
            else:
                root.element = self.pre_successor(root)
                root.left = self._remove(root.left, root.element)

        root.height = self.height(root)
        return root

    def height(self, root: AVLNode):
        """计算节点的高度

        Args:
            node (AVLNode): 根结点
        """
        if not root:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1

    @staticmethod
    def balance_factor(node_1: AVLNode, node_2: AVLNode) -> int:
        """计算平衡因子

        Args:
            node_1 (AVLNode): 节点 1
            node_2 (AVLNode): 节点 2

        Returns:
            int: 平衡因子
        """
        height_1, height_2 = 0, 0
        if node_1:
            height_1 = node_1.height

        if node_2:
            height_2 = node_2.height

        return abs(height_1 - height_2)


@measure
def find(tree, element):
    return tree.get(element)


def main():
    import random

    tree = AVLTree()
    for i in range(10):
        i = random.randint(0, 10)
        tree.put(i)

    tree.format_out()
    tree.remove(tree.root, 3)
    tree.format_out()


if __name__ == "__main__":
    main()
