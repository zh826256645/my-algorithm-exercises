# -*- coding: utf-8 -*-
"""
伸展树

被查询频率越高的节点会越靠近树根

@File    :   splay_tree.py
@Time    :   2020/09/12 10:25:55
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   None
"""
from model.binary_tree import BinarySearchTree, BiTNode


class SplayTree(BinarySearchTree):
    """ 伸展树 """

    def rotate_right(self, root: BiTNode) -> BiTNode:
        """右旋转

        :param BiTNode root: 根节点
        :return BiTNode: 新的根节点
        """
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        return new_root

    def rotate_left(self, root: BiTNode) -> BiTNode:
        """左旋转

        :param BiTNode root: 根节点
        :return BiTNode: 新的根节点
        """
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        return new_root

    def rotate_double_right(self, root: BiTNode) -> BiTNode:
        """进行两次右旋
        当搜索节点是父节点的左节点，父节点是祖父节点的左节点时

        例如：搜索节点 [1]

              [4]            [4]            [1]
             /              /                  \
           [2]    -右旋->  [1]     -右旋->      [4]
          /                  \                /
        [1]                  [2]            [2]

        :param BiTNode root: 根节点
        :return BiTNode: 新的根节点
        """
        new_root = self.rotate_right(root)
        new_root = self.rotate_right(new_root)

        return new_root

    def rotate_double_left(self, root: BiTNode) -> BiTNode:
        """进行两次左旋
        当搜索节点是父节点的右节点，父节点是祖父节点的右节点时

        例如: 搜索节点 [4]

        [1]                  [1]                [4]
           \                    \              /
           [2]    -左旋->       [4]  -左旋->  [1]
              \                /                \
              [4]            [2]                [2]

        :param BiTNode root: 根节点
        :return BiTNode: 新的更节点
        """
        new_root = self.rotate_left(root)
        new_root = self.rotate_left(new_root)

        return new_root

    def rotate_right_left(self, root: BiTNode) -> BiTNode:
        """先右旋再左旋
        当前节点是父节点的左节点，父节点是祖父节点的右节点

        例如：搜索节点 [3]

        [2]            [2]                  [3]
           \              \                /   \
           [4]  -右旋->    [3]    -左旋-> [2]   [4]
          /                  \
        [3]                  [4]

        :param BiTNode root: 根节点
        :return BiTNode: 新的根节点
        """
        root.right = self.rotate_right(root.right)
        new_root = self.rotate_left(root)

        return new_root

    def rotate_left_right(self, root: BiTNode) -> BiTNode:
        """先左旋再右旋
        当前节点是父节点的右节点，父节点是祖父节点的左节点

        例如: 搜索节点 [2]

          [3]              [3]           [2]
          /                /            /   \
        [1]    -左旋->    [2]  -右旋-> [1]    [3]
           \             /
           [2]         [1]
        :param BiTNode root: 根节点
        :return BiTNode: 新的根节点
        """
        root.left = self.rotate_left(root.left)
        new_root = self.rotate_right(root)

        return new_root

    def get(self, element, node=None) -> BiTNode:
        """查找第一个匹配元素的节点

        Keyword arguments:
        element -- 匹配的元素
        node -- 开始的节点
        Return: 节点
        """
        current = node
        if not current:
            current = self.root

        father_path = list()
        while current:
            if current.element == element:
                self.root = self.splay(father_path, current)
                return current

            father_path.append(current)
            if current.element > element:
                current = current.left
            else:
                current = current.right

    def splay(self, father_path: list, current: BiTNode):
        """将当前节点变为根节点

        :param list father_path: 从根节点到当前节点的路径
        :param BiTNode current: 当前节点
        """
        while father_path:
            parent = father_path.pop()
            if father_path:
                grandpa = father_path.pop()
                if father_path:
                    if father_path[-1].left == grandpa:
                        father_path[-1].left = self.splay_with_grandpa(current, parent, grandpa)
                    else:
                        father_path[-1].right = self.splay_with_grandpa(current, parent, grandpa)
                else:
                    self.splay_with_grandpa(current, parent, grandpa)
            elif current == parent.left:
                self.rotate_right(parent)
            else:
                self.rotate_left(parent)
        return current

    def splay_with_grandpa(self, current: BiTNode, parent: BiTNode, grandpa: BiTNode) -> BiTNode:
        """将当前节点跟祖父节点调换

        :param BiTNode current: 当前节点
        :param BiTNode parent: 父节点
        :param BiTNode grandpa: 祖父节点
        :return BiTNode: 新的根节点
        """
        _type = 'l' if parent == grandpa.left else 'r'
        _type += 'l' if current == parent.left else 'r'

        if _type == 'll':
            return self.rotate_double_right(grandpa)
        elif _type == 'rr':
            return self.rotate_double_left(grandpa)
        elif _type == 'rl':
            return self.rotate_right_left(grandpa)
        else:
            return self.rotate_left_right(grandpa)


def main():
    tree = SplayTree()
    for i in range(10):
        tree.put(i)

    tree.format_out()
    print(tree.get(9))
    tree.format_out()
    print(tree.get(5))
    tree.format_out()


if __name__ == "__main__":
    main()
