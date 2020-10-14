# -*- coding: utf-8 -*-
"""
跳表

@File    :   skip_list.py
@Time    :   2020/10/07 17:46:16
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   None
"""
import random


class SkipListNode:
    """跳表的节点

    """
    INF = '+oo'
    SUP = '-oo'

    def __init__(self, key, value) -> None:
        """初始化

        :param key: 节点的键
        :param value: 节点的值
        :param next_node: 下一个节点
        """
        self.key = key
        self.value = value

        self.left = None
        self.right = None
        self.up = None
        self.down = None

    def __str__(self) -> str:
        return f'SkipListNode[{self.key}:{self.value}]'


class SkipList:
    """跳表

    """
    def __init__(self) -> None:
        head = SkipListNode(SkipListNode.SUP, None)
        tail = SkipListNode(SkipListNode.INF, None)
        head.right = tail
        tail.left = head

        self.head = head
        self.tail = tail

        self.num = 0
        self.max_level = 0

    def __str__(self) -> str:
        head = self.head
        _str = ''
        while head:
            current = head.right
            nodes = list()
            while current and current.key != SkipListNode.INF:
                nodes.append(str(current))
                current = current.right

            _str += ' -> '.join(nodes)
            _str += '\n'

            head = head.down

        return _str

    @property
    def r(self):
        return random.uniform(0, 1)

    def find(self, key) -> SkipListNode:
        """查找 Node key 值大于等于要查找 key 值的节点

        1. 如果 key 值在跳表中存在，则返回该对象的底层节点
        2. 如果 key 值在跳表中不存在，则返回跳表中 key 值小于 key，并且 key 相差最小的底层节点

        :param key: 键
        :return SkipListNode: 对于的节点
        """
        current = self.head

        while True:
            # 从左往右查找，直到右边的节点大于要找的 key 值
            while current.right.key != SkipListNode.INF and current.right.key <= key:
                current = current.right

            # 如果有更低层次的节点，则向低层移动
            if current.down:
                current = current.down
            else:
                break

        return current

    def get(self, key):
        """获取键对应的值

        :param key: 查找的键
        """
        node = self.find(key)
        if node.key == key:
            return node.value
        return None

    def put(self, key, value):
        """插入新的键值

        1. 如果 key 在跳表中存在，则修改对于节点 value 的值
        2. 如果 key 不存在，则增加新的节点，并且更加 r 的值，决定新加入节点的高度
        3. 当新加的节点高度达到跳表的最大 level，需要加入一层空白层（只有 -oo 和 +oo 没有别的节点）

        :param key: 键
        :param value: 值
        """
        current = self.find(key)

        if current.key == key:
            current.value = value
            return

        node = SkipListNode(key, value)
        node.left = current
        node.right = current.right
        current.right.left = node
        current.right = node

        level = 0
        break_status = True
        while self.r < 0.5 and break_status:

            if level >= self.max_level:
                break_status = False
                self._add_empty_level()

            while current.up is None:
                current = current.left

            current = current.up

            upper_level_node = SkipListNode(key, None)

            upper_level_node.left = current
            upper_level_node.right = current.right
            current.right.left = upper_level_node
            current.right = upper_level_node

            node.up = upper_level_node
            upper_level_node.down = node

            node = upper_level_node
            level += 1

        self.num += self.num

    def _add_empty_level(self):
        """加入空层

        """
        head = SkipListNode(SkipListNode.SUP, None)
        tail = SkipListNode(SkipListNode.INF, None)

        head.right = tail
        tail.left = head

        head.down = self.head
        tail.down = self.tail

        self.head.up = head
        self.tail.up = tail

        self.head = head
        self.tail = tail

        self.max_level += 1

    def remove(self, key):
        """移除 key 对应的节点

        :param key: 键
        """
        node = self.find(key)
        if node.key != key:
            return

        value = node.value
        while node:
            node.right.left = node.left
            node.left.right = node.right
            node = node.up

        return value


def test():
    skip_list = SkipList()

    # num = str(random.randint(0, 1000000))
    # for i in range(1000000):
    #     skip_list.put(str(i), i)

    # import time
    # t1 = time.time()
    # print(skip_list.get(num))
    # print(f'跳跃表查找 {num} 用时：{time.time() - t1}')

    # del skip_list
    # nums = list()
    # for i in range(1000000):
    #     nums.append(i)

    # t1 = time.time()
    # num = int(num)
    # for i in nums:
    #     if i == num:
    #         print(i)
    #         print(f'list 遍历查找 {num} 用时：{time.time() - t1}')
    #         break

    for i in range(10):
        skip_list.put(str(i), i)

    print(skip_list)
    skip_list.remove('4')
    print(skip_list)


if __name__ == "__main__":
    test()
