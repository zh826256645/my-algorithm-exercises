# -*- encoding: utf-8 -*-
"""
二叉树

@File    :   binary_tree.py
@Time    :   2020/08/01 16:34:06
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   None
"""

import random

# 树枝
PREFIX_BRANCH = "├"
# 树干
PREFIX_TRUNK = "│ "
# 叶子
PREFIX_LEAF = "└"
# 空
PREFIX_EMP = "  "
# 左
PREFIX_LEFT = "─L─"
# 右
PREFIX_RIGHT = "─R─"


class BiTNode:
    """二叉树节点

    """

    def __init__(self, element=None, left=None, right=None) -> None:
        """初始化

        Keyword arguments:
        element -- 节点元素
        left -- 左节点
        right -- 右节点
        """
        self.element = element
        self.left = left
        self.right = right

    def __lt__(self, node):
        return self.element < node.element

    def __gt__(self, node):
        return self.element > node.element

    def __eq__(self, node):
        return self.element == node.element

    def __str__(self) -> str:
        return f'BiTNode[{self.element}]'


class BinaryTree:
    """二叉树

    """

    def __init__(self, root=None) -> None:
        """初始化二叉树

        Keyword arguments:
        root -- 根节点
        Return: return_description
        """

        self.root = root

    def put(self, element) -> bool:
        """插入节点

        Keyword arguments:
        element -- 节点值
        Return: return_description
        """
        node = BiTNode(element)
        if not self.root:
            self.root = node
        else:
            current = self.root
            while current:
                if node < current:
                    if not current.left:
                        current.left = node
                        break
                    else:
                        current = current.left
                else:
                    if not current.right:
                        current.right = node
                        break
                    else:
                        current = current.right

    def get(self, element, node=None):
        """查找第一个匹配元素的节点

        Keyword arguments:
        element -- 匹配的元素
        node -- 开始的节点
        Return: return_description
        """
        current = node
        if not current:
            current = self.root

        while current:
            if current.element == element:
                return current
            elif current.element > element:
                current = current.left
            else:
                current = current.right

    def delete(self, element, node=None):
        """删除第一个匹配的节点

        Keyword arguments:
        argument -- description
        Return: return_description
        """

    def pre_order(self, node) -> str:
        """前序遍历

        Keyword arguments:
        node -- 节点
        Return: return_description
        """
        _str = ''
        if node:
            _str += f'-> {str(node)}'
            _str += self.pre_order(node.left)
            _str += self.pre_order(node.right)
        return _str

    def in_order(self, node) -> str:
        """中序遍历

        Keyword arguments:
        node -- 节点
        Return: return_description
        """
        _str = ''
        if node:
            _str += self.in_order(node.left)
            _str += f'-> {str(node)}'
            _str += self.in_order(node.right)
        return _str

    def post_order(self, node) -> str:
        """后续遍历

        Keyword arguments:
        node -- 节点
        Return: return_description
        """
        _str = ''
        if node:
            _str += self.post_order(node.left)
            _str += self.post_order(node.right)
            _str += f'-> {str(node)}'
        return _str

    def lever_order(self, node=None) -> str:
        """层次遍历

        Keyword arguments:
        node -- 节点
        Return: return_description
        """
        _str = ''

        current = node
        if not current:
            current = self.root

        lever = list()
        lever.append(current)
        while lever:
            last_lever = list()
            for node in lever:
                _str += f'-> {str(node)}'
                if node.left:
                    last_lever.append(node.left)

                if node.right:
                    last_lever.append(node.right)
            lever = last_lever

        return _str

    def remove(self, element, node=None) -> bool:
        """移除第一个匹配元素的节点

        移除的节点无左右子节点(叶子节点)
        移除的节点无左子节点
        移除的节点无右子节点
        移除的节点同时有左右节点

        Keyword arguments:
        element -- 元素
        node -- 节点
        Return: return_description
        """
        if not node:
            return None

        pass

    @staticmethod
    def has_child(node):
        """判断节点是否有子节点

        Keyword arguments:
        node -- 节点
        Return: return_description
        """
        if node.right or node.left:
            return True
        return False

    def format_out(self, node=None) -> str:
        """格式化输出

        Keyword arguments:
        node -- 节点
        Return: return_description
        """
        if not node:
            node = self.root

        print(node)
        self._format_out(node)

    def _format_out(self, node, prefix=None):
        if not prefix:
            prefix = ''
        else:
            prefix = prefix.replace(PREFIX_BRANCH, PREFIX_TRUNK)
            prefix = prefix.replace(PREFIX_LEAF, PREFIX_EMP)

        if self.has_child(node):
            if node.right:
                print(prefix + PREFIX_BRANCH + PREFIX_RIGHT + str(node.right))
                if self.has_child(node.right):
                    self._format_out(node.right, prefix + PREFIX_BRANCH)
            else:
                print(prefix + PREFIX_BRANCH + PREFIX_RIGHT)

            if node.left:
                print(prefix + PREFIX_LEAF + PREFIX_LEFT + str(node.left))
                if self.has_child(node.left):
                    self._format_out(node.left, prefix + PREFIX_LEAF)
            else:
                print(prefix + PREFIX_LEAF + PREFIX_LEFT)


def main():
    tree = BinaryTree()
    for i in range(10):
        tree.put(random.randint(0, 100))

    _str = tree.pre_order(tree.root)
    print(_str)
    _str = tree.in_order(tree.root)
    print(_str)
    _str = tree.post_order(tree.root)
    print(_str)
    _str = tree.lever_order(tree.root)
    print(_str)
    tree.format_out()


if __name__ == "__main__":
    main()
