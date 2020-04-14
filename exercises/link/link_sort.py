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
from model import Link, init_link


@measure
def insertion_sorting(link: Link) -> Link:
    """
    插入排序

    链表的长度为 1000 --- Total execution time: 286 ms
    链表的长度为 10000 --- Total execution time: 30442 ms

    Keyword arguments:
    argument -- description
    Return: return_description
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
                link.head_node = new_head_node

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


if __name__ == "__main__":
    link = init_link(10000, True)
    link = insertion_sorting(link)
