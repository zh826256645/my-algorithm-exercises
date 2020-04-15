# -*- encoding: utf-8 -*-
"""
链表排序练习

@File    :   link_sort.py
@Time    :   2020/04/14 :46:33
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   None
"""
from utils import measure
from model import Link, Node, init_link


@measure
def insertion_sorting(link: Link) -> Link:
    """
    插入排序

    测试:
        链表的长度为 1000 --- Total execution time: 286 ms
        链表的长度为 10000 --- Total execution time: 30442 ms

    leetcode:
        执行用时 :2564 ms, 在所有 Python3 提交中击败了 9.48% 的用户
        内存消耗 :15.3 MB, 在所有 Python3 提交中击败了 12.50% 的用户

    问题:
        1.使用了新的空间
        2.进行了多次的比较

    优化:
        1.在不断链的情况下进行排序
        2.减少比较次数
    """

    new_head_node = None
    current_node = link.head_node

    while current_node:
        next_node = current_node.next_node
        current_node.next_node = None

        if not new_head_node:
            new_head_node = current_node
        else:
            node = new_head_node
            last_node = None
            while node:
                if node > current_node:
                    current_node.next_node = node
                    if not last_node:
                        new_head_node = current_node
                    else:
                        last_node.next_node = current_node
                    break

                elif not node.next_node:
                    node.next_node = current_node
                    break

                last_node = node
                node = node.next_node

        current_node = next_node

    link.head_node = new_head_node
    return link


@measure
def optimize_insertion_sorting(link: Link) -> Link:
    """
    优化插入排序

    测试:
        链表的长度为 1000 --- Total execution time: 235 ms
        链表的长度为 10000 --- Total execution time: 23785 ms

    leetcode:
        执行用时 :220 ms, 在所有 Python3 提交中击败了 74.71% 的用户
        内存消耗 :15.3 MB, 在所有 Python3 提交中击败了 12.50% 的用户
    """
    current_node = link.head_node
    head_node = Node(0, link.head_node)

    while current_node and current_node.next_node:
        if current_node <= current_node.next_node:
            current_node = current_node.next_node
            continue

        head_current_node = head_node
        while head_current_node.next_node < current_node.next_node:
            head_current_node = head_current_node.next_node

        _current_node = current_node.next_node
        current_node.next_node = _current_node.next_node
        _current_node.next_node = head_current_node.next_node
        head_current_node.next_node = _current_node

    link.head_node = head_node.next_node
    return link


if __name__ == "__main__":
    link = init_link(10000, True)
    # link = insertion_sorting(link)
    link = optimize_insertion_sorting(link)
