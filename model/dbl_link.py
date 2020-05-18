# -*- encoding: utf-8 -*-
"""
双向循环链表

@File    :   dbl_link.py
@Time    :   2020/05/12 00:59:22
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   双向循环链表数据结构
"""

from model.link import Node


class DblNode(Node):

    def __init__(self, value=None, prev_node=None, next_node=None):
        """初始化节点

        Keyword Arguments:
            value {[type]} -- 节点的值 (default: {None})
            prev_node {DblNode} -- 上一个节点 (default: {None})
            next_node {DblNode} -- 下一个节点 (default: {None})
        """
        super(DblNode, self).__init__(value, next_node)
        self.prev_node = prev_node

    def get_prev(self):
        """ 获取上一个节点 """
        return self.prev_node


class DblLink:

    def __init__(self, head_node: DblNode = None):
        """初始化链表

        当头节点的前驱节点和后继节点为空时，将头节点的前驱和后继节点指向自己

        Arguments:
            head_node {DblNode} -- 头节点 (default: {None})
        """
        self.length = 0
        if head_node:
            head_node.prev_node = head_node
            head_node.next_node = head_node
            self.length += 1

        self.head_node = head_node

    def add_node(self, node: DblNode) -> bool:
        """添加节点

        Arguments:
            node {DblNode} -- 添加的节点

        Returns:
            bool -- 添加结果
        """
        if node:
            if not self.head_node:
                node.prev_node = node
                node.next_node = node
                self.head_node = node
            else:
                tail_node = self.head_node.prev_node
                tail_node.next_node = node
                node.prev_node = tail_node
                self.head_node.prev_node = node
                node.next_node = self.head_node

            self.length += 1
            return True
        return False

    def remove_node(self, index: int) -> Node:
        """删除节点

        Arguments:
            index {int} -- 删除节点的位置

        Returns:
            Node -- 删除的节点
        """
        current_node = self.head_node
        step = 0

        if not self.head_node or index > self.length - 1:
            return None

        while current_node and step <= self.length - 1:
            if step != index:
                current_node = current_node.next_node
                step += 1
            else:
                if self.head_node == current_node:
                    self.head_node = None
                else:
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node

                current_node.prev_node = None
                current_node.next_node = None
                self.length -= 1
                return current_node
        return None

    def get_nodes(self) -> list:
        """获取所有节点

        Returns:
            list -- 所有节点的列表
        """
        nodes = list()
        current_node = self.head_node
        while current_node:
            nodes.append(current_node)
            current_node = current_node.next_node
            if current_node == self.head_node:
                break

        return nodes

    def __str__(self):
        nodes = self.get_nodes()
        return f'DblLink[{" <-> ".join([str(node) for node in nodes])}]'

    def __len__(self):
        return self.length


if __name__ == "__main__":
    link = DblLink()
    link.add_node(DblNode(0))
    link.add_node(DblNode(1))
    link.add_node(DblNode(2))
    link.add_node(DblNode(3))
    print(link)
    link.remove_node(2)
    print(link)
    link.remove_node(2)
    print(link)
