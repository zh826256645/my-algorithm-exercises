# -*- coding: utf-8 -*-
"""
堆树

是一个随机附加域满足堆的性质的二叉树

@File    :   treap.py
@Time    :   2020/09/10 16:04:56
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   None
"""
import random

from model.binary_tree import BinarySearchTree, BiTNode


class TreapNode(BiTNode):

    def __init__(self, element=None, left=None, right=None, priority=0) -> None:
        """初始化节点

        :param element: 节点元素
        :param left: 左节点
        :param right: 右节点
        :param int priority: 优先级
        """
        super().__init__(element, left, right)
        if priority:
            self.priority = priority
        else:
            self.priority = random.randint(0, 32767)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}[{self.element}:{self.priority}]'


class Treap(BinarySearchTree):

    def rotate_left(self, root: TreapNode) -> TreapNode:
        """左旋

        :param TreapNode root: 根结点
        :return TreapNode: 旋转后的根节点
        """
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        return new_root

    def rotate_right(self, root: TreapNode) -> TreapNode:
        """右旋

        :param TreapNode root: 根结点
        :return TreapNode: 旋转后的根结点
        """
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        return new_root

    def put(self, element):
        node = TreapNode(element)
        if not self.root:
            self.root = node
        else:
            self.root = self._put(self.root, node)

    def _put(self, root: TreapNode, node: TreapNode) -> TreapNode:
        if not root:
            root = node

        elif root > node:
            root.left = self._put(root.left, node)
            if root.left.priority < root.priority:
                root = self.rotate_right(root)

        else:
            root.right = self._put(root.right, node)
            if root.right.priority > root.priority:
                root = self.rotate_left(root)

        return root

    def remove(self, node: BiTNode, key) -> BiTNode:
        """移除节点

        1.当被移除的根节点无左子节点时，直接让右子节点成为新的根节点
        2.当被移除的根节点无右子节点时，直接让左子节点成为新的根节点
        3.当被移除的根节点同时存在左右子节点时
            1) 当左子节点的优先级小于右子节点时，先对根节点进行右旋，再删除新根节点的右子节点（原根节点）
            2) 当左子节点的优先级大于等于右子节点时，先对根节点进行左旋，再删除新根节点的左子节点（原根节点）

        :param BiTNode node: 根节点
        :param key: 移除节点的 key
        :return BiTNode: 新的根节点
        """
        if node:
            if node.element > key:
                node.left = self.remove(node.left, key)
            elif node.element < key:
                node.right = self.remove(node.right, key)
            else:
                if not node.left:
                    node = node.right
                elif not node.right:
                    node = node.left
                else:
                    if node.left.priority < node.right.priority:
                        node = self.rotate_right(node)
                        node.right = self.remove(node.right, key)
                    else:
                        node = self.rotate_left(node)
                        node.left = self.remove(node.left, key)
        return node


def main():
    tree = Treap()

    for i in range(10):
        # i = random.randint(0, 10)
        tree.put(i)

    tree.format_out()
    tree.remove(tree.root, 6)
    tree.format_out()

    print(tree.get(7))


if __name__ == "__main__":
    main()
