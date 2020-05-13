# -*- encoding: utf-8 -*-
"""
链表数据结构

@File    :   link.py
@Time    :   2020/04/11 21:51:37
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   None
"""


class Node:
    """ 节点 """
    def __init__(self, value=None, next_node=None):
        self.element = value
        self.next_node = next_node

    def get_element(self):
        "获取节点的元素"
        return self.element

    def get_next(self):
        "获取下一个节点"
        return self.next_node

    def __str__(self):
        return f'{self.__class__.__name__}[element={self.element}]'

    def __gt__(self, other_node):
        return self.element > other_node.element

    def __lt__(self, other_node):
        return self.element < other_node.element

    def __ge__(self, other_node):
        return self.element >= other_node.element

    def __le__(self, other_node):
        return self.element <= other_node.element


class Link:
    """ 链表 """
    def __init__(self, head_node=None):
        "初始化"
        self.head_node = head_node
        self.length = 1 if head_node else 0

    def add_node(self, node: Node) -> bool:
        "添加节点"
        if not self.head_node:
            self.head_node = node
        else:
            current_node = self.head_node
            while current_node.next_node:
                current_node = current_node.next_node

            current_node.next_node = node

        self.length += 1
        return True

    def remove_node(self, index: int) -> bool:
        "删除节点"
        _index = 0
        current_node = self.head_node
        last_node = None
        status = False
        if index <= self.length - 1:
            while current_node:
                if _index == index:
                    if not last_node:
                        self.head_node = current_node.next_node
                    else:
                        last_node.next_node = current_node.next_node
                    status = True
                    break
                else:
                    last_node = current_node
                    current_node = current_node.next_node
                    _index += 1
        if status:
            self.length -= 1
        return status

    def find_node(self, index: int) -> Node:
        "查找节点"
        status = self.has_cycle()
        if status:
            raise Exception('链表存在环')

        _index = 1
        current_node = self.head_node
        if index <= self.length:
            while current_node:
                if _index == index:
                    return current_node
                else:
                    current_node = current_node.next_node
                    _index += 1
        return None

    def find_last_node(self, reverse_index: int):
        "通过 length 属性查找倒数第几个节点"
        index = self.length - reverse_index + 1

        if index > 0:
            return self.find_node(index)
        return None

    def get_nodes(self) -> list:
        "获取所有节点"
        status = self.has_cycle()
        if status:
            raise Exception('链表存在环')

        nodes = list()
        current_node = self.head_node
        while current_node:
            nodes.append(current_node)
            current_node = current_node.next_node

        return nodes

    def has_cycle(self) -> bool:
        "判断链表是否有环"
        first_node = self.head_node
        second_node = self.head_node
        while second_node and second_node.next_node:
            first_node = first_node.next_node
            second_node = second_node.next_node.next_node
            if first_node == second_node:
                return True
        return False

    def __str__(self):
        nodes = self.get_nodes()
        return f'Link[{" -> ".join([str(node) for node in nodes])}]'
