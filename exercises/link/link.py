# -*- encoding: utf-8 -*-
"""
链表练习

@File    :   link_exercises.py
@Time    :   2020/04/13 23:05:41
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   None
"""
from model import init_link, Link, Node


def find_last_node(link, reverse_index: int):
    " 不使用 length 属性，查询倒数的节点 "
    first_node = link.head_node
    second_node = link.head_node
    for i in range(reverse_index):
        if not second_node:
            return None
        second_node = second_node.next_node

    while second_node:
        second_node = second_node.next_node
        first_node = first_node.next_node
    return first_node


def find_middle_node(link: Link) -> Node:
    " 查找中间的节点 "
    first_node = link.head_node
    second_node = link.head_node
    while second_node.next_node and second_node.next_node.next_node:
        first_node = first_node.next_node
        second_node = second_node.next_node.next_node
    return first_node


def reverse_link(link: Link) -> Link:
    " 反转链表 "
    new_head_node = None
    current_node = link.head_node
    while current_node:
        next_node = current_node.next_node
        current_node.next_node = new_head_node
        new_head_node = current_node
        current_node = next_node

    link.head_node = new_head_node
    return link


def reverse_print(node: Node):
    " 反转打印 "
    if node.next_node:
        reverse_print(node.next_node)

    print(f'{node} -> ', end='')


def get_cycle_length(link: Link) -> int:
    """
    获取环的长度

    环的长度即为相遇时 first 走过的长度
    """
    first_node = link.head_node
    second_node = link.head_node
    length = 0
    while first_node and first_node.get_next and second_node and second_node.get_next:
        first_node = first_node.next_node
        second_node = second_node.next_node.next_node
        length += 1
        if first_node == second_node:
            return length
    return 0


if __name__ == "__main__":
    # link = init_link(10)
    # print(link)
    # node = find_last_node(link, 11)
    # print(node)
    # node = link.find_node(11)
    # print(node)
    # node = link.find_last_node(11)
    # print(node)
    # node = find_middle_node(link)
    # print(f'middle node: {node}')
    # _link = reverse_link(init_link(20))
    # print(f'reverse_link: {_link}')
    # print('reverse_print')
    # reverse_print(init_link(10).head_node)
    print()
    _link = init_link(10)
    # 设置环
    _link.find_node(10).next_node = _link.find_node(5)
    print(f'环的长度为：{get_cycle_length(_link)}')
