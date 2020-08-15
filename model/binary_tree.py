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


class BinarySearchTree:
    """二叉搜索树

    满足以下条件
        1. 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
        2. 若任意节点的右子树不空，则右子树上所有节点的值均大于或等于它的根节点的值；
        3. 任意节点的左、右子树也分别为二叉查找树；

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

    def remove(self, node: BiTNode, key) -> BiTNode:
        """移除第一个匹配元素的节点

        三种情况：
            1.移除的节点无左右子节点(叶子节点)：直接移除
            2.移除的节点有右子节点：找出右子节点中最小的继任者，替换要移除的节点
            3.移除的节点只有左子节点：找出左子节点中最大的继任者，替换要移除的节点

        Keyword arguments:
        node -- 节点
        key -- 匹配的 key
        """
        if not node:
            return None

        if node.element > key:
            node.left = self.remove(node.left, key)
        elif node.element < key:
            node.right = self.remove(node.right, key)
        else:
            if not node.left and not node.right:
                node = None
            elif node.right:
                node.element = self.successor(node)
                node.right = self.remove(node.right, node.element)
            else:
                node.element = self.pre_successor(node)
                node.left = self.remove(node.left, node.element)

        return node

    @staticmethod
    def successor(node):
        """获取节点右节点中最小的继任者

        Keyword arguments:
        node -- 节点
        Return: 节点的值
        """

        node = node.right
        while node.left:
            node = node.left
        return node.element

    @staticmethod
    def pre_successor(node):
        """获取节点左子节点中最大的继承者

        Keyword arguments:
        node -- 节点
        Return: 节点的值
        """

        node = node.left
        while node.right:
            node = node.right
        return node.element

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
    tree = BinarySearchTree()
    tree.put(5)
    tree.put(3)
    tree.put(4)
    tree.put(2)
    tree.put(1)
    tree.put(7)
    tree.put(6)
    tree.put(8)
    tree.put(9)

    tree.format_out()

    tree.remove(tree.root, 1)

    tree.format_out()

    tree.remove(tree.root, 5)

    tree.format_out()

    tree.remove(tree.root, 10)

    tree.format_out()

    print(tree.in_order(tree.root))


if __name__ == "__main__":
    main()
