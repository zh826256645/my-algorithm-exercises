# -*- encoding: utf-8 -*-
"""
LRU 缓存类


@File    :   lru_cache.py
@Time    :   2020/08/01 16:34:20
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   使用双向链表 + 字典实现缓存机制
"""

from model.dbl_link import DblNode, DblLink


class LRUNode(DblNode):

    def __init__(self, value=None, prev_node=None, next_node=None, key=None):
        super().__init__(value, prev_node, next_node)
        self.key = key

    def __str__(self) -> str:
        return f'{self.__class__.__name__}[key={self.key}, value={self.element}]'


class LRUCache:

    def __init__(self, capacity=10) -> None:
        self.key_map = dict()
        self.capacity = 10
        self.head = LRUNode()
        self.tail = LRUNode()
        self.head.next_node = self.tail
        self.tail.prev_node = self.head
        self.size = 0

    def put(self, key: str, value) -> None:
        """添加元素

        Keyword arguments:
        key -- 键
        value -- 值
        """
        node = self.key_map.get(key)
        if not node:
            node = LRUNode(key=key, value=value)
            self.add_to_head(node)
            self.key_map[key] = node

            self.size += 1
            if self.size > self.capacity:
                node = self.remove_tail_node()
                self.key_map.pop(node.key)

                self.size -= 1
        else:
            node.element = value
            self.move_to_head(node)

    def get(self, key):
        """获取键对应的值

        Keyword arguments:
        key -- 键
        Return: 值
        """
        node = self.key_map.get(key)
        if not node:
            return -1

        self.move_to_head(node)
        return node.value

    def add_to_head(self, node: LRUNode) -> bool:
        """添加到头节点

        Keyword arguments:
        node -- 节点
        Return: 操作状态
        """
        if node:
            node.prev_node = self.head
            node.next_node = self.head.next_node
            self.head.next_node.prev_node = node
            self.head.next_node = node

            return True
        return False

    def move_to_head(self, node: LRUNode) -> bool:
        """移动节点到头部

        Keyword arguments:
        node -- 节点
        Return: 操作状态
        """
        if node:
            self.remove_node(node)
            self.add_to_head(node)
        return False

    def remove_node(self, node: LRUNode) -> DblNode:
        """移除节点

        Keyword arguments:
        node -- 节点
        Return: 操作状态
        """
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node

    def remove_tail_node(self) -> LRUNode:
        """移除尾部节点

        Return: 操作状态
        """
        node = self.tail.prev_node
        self.remove_node(node)
        return node


def main():
    cache = LRUCache()
    link = DblLink()
    link.head_node = cache.head

    for i in range(10):
        cache.put(chr(97 + i), 97 + i)

    print(link)

    cache.put('a', 299)

    print(link)

    cache.put('z', 2999)

    print(link)


if __name__ == "__main__":
    main()
