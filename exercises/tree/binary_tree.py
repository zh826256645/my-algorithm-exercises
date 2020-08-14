# -*- encoding: utf-8 -*-
"""
二叉树的练习

@File    :   binary_tree.py
@Time    :   2020/08/14 11:36:30
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   None
"""
from exercises.tree import init_tree
from model.binary_tree import BiTNode


def get_tree_depth(root: BiTNode) -> int:
    """获取树的最大深度

    Keyword arguments:
    root -- 开始的根结点
    Return: 深度值
    """
    if not root:
        return 0

    left_depth = get_tree_depth(root.left) + 1
    right_depth = get_tree_depth(root.right) + 1

    return max(left_depth, right_depth)


def get_tree_width(root: BiTNode) -> int:
    """获取树的最大宽度

    Keyword arguments:
    root -- 开始的根节点
    Return: 宽度值
    """
    if not root:
        return 0

    level_nodes = list()
    level_nodes.append(root)
    current_level_width = 1
    last_level_width = 0
    max_width = 1

    while level_nodes:
        while current_level_width > 0:
            node = level_nodes.pop()

            if node.left:
                level_nodes.insert(0, node.left)
                last_level_width += 1

            if node.right:
                level_nodes.insert(0, node.right)
                last_level_width += 1

            current_level_width -= 1

        max_width = max(max_width, last_level_width)
        current_level_width, last_level_width = last_level_width, 0

    return max_width


def main():
    tree = init_tree(random_tree=True)
    tree.format_out()
    print(get_tree_width(tree.root))


if __name__ == "__main__":
    main()
