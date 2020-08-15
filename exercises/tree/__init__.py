# -*- encoding: utf-8 -*-
"""
树数据结构的练习

@File    :   __init__.py
@Time    :   2020/08/14 11:35:22
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   二叉树、平衡树、红黑树
"""
import random

from model.binary_tree import BinarySearchTree


def init_tree(random_tree=False, num=10) -> BinarySearchTree:
    tree = BinarySearchTree()

    if random_tree:
        for i in range(num):
            tree.put(random.randint(0, i))
    else:
        tree.put(5)
        tree.put(3)
        tree.put(4)
        tree.put(2)
        tree.put(1)
        tree.put(7)
        tree.put(6)
        tree.put(8)
        tree.put(9)
    return tree
