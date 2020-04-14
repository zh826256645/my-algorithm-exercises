# -*- encoding: utf-8 -*-
"""
各种数据结构

@File    :   __init__.py
@Time    :   2020/04/11 21:58:44
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   None
"""
import random

from model.link import Link, Node


def init_link(length: int = 10, is_random=False) -> Link:
    "初始化 Link 对象"
    link = Link()
    for i in range(length):
        if is_random:
            link.add_node(Node(random.randint(0, length)))
        else:
            link.add_node(Node(i))
    return link
