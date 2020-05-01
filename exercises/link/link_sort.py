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
def insertion_sort(link: Link) -> Link:
    """
    插入排序

    测试:
        链表的长度为 1000 --- Total execution time: 286 ms
        链表的长度为 10000 --- Total execution time: 30442 ms

    leetcode:
        link: https://leetcode-cn.com/problems/insertion-sort-list/
        执行用时: 2564 ms, 在所有 Python3 提交中击败了 9.48% 的用户
        内存消耗: 15.3 MB, 在所有 Python3 提交中击败了 12.50% 的用户

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
def optimize_insertion_sort(link: Link) -> Link:
    """
    优化插入排序

    测试:
        链表的长度为 1000 --- Total execution time: 235 ms
        链表的长度为 10000 --- Total execution time: 23785 ms

    leetcode:
        link: https://leetcode-cn.com/problems/insertion-sort-list/
        执行用时: 220 ms, 在所有 Python3 提交中击败了 74.71% 的用户
        内存消耗: 15.3 MB, 在所有 Python3 提交中击败了 12.50% 的用户
    """
    head_node = Node(0, link.head_node)

    current_node = link.head_node
    while current_node and current_node.next_node:
        if current_node <= current_node.next_node:
            current_node = current_node.next_node
            continue

        start_node = head_node
        while start_node.next_node < current_node.next_node:
            start_node = start_node.next_node

        temp_node = current_node.next_node
        current_node.next_node = temp_node.next_node
        temp_node.next_node = start_node.next_node
        start_node.next_node = temp_node

    link.head_node = head_node.next_node
    return link


@measure
def selection_sort(link: Link) -> Link:
    """
    选择排序

    说明:
        1. 交换任意两个节点，需要用定位到它们的父节点
        2. 要分相邻和不相邻两种情况处理

    测试:
        链表的长度为 1000 --- Total execution time: 656 ms
        链表的长度为 10000 --- Total execution time: 67671 ms
    """
    head_node = Node(0, link.head_node)

    start_node = head_node
    while start_node.next_node:
        parent_node = None

        current_node = start_node.next_node
        while current_node.next_node:
            if current_node.next_node < start_node.next_node:
                if not parent_node or parent_node.next_node > current_node.next_node:
                    parent_node = current_node

            current_node = current_node.next_node

        if parent_node:
            if parent_node.next_node == start_node.next_node.next_node:
                # 相邻
                swap_node = parent_node.next_node
                start_node.next_node.next_node = swap_node.next_node
                swap_node.next_node = start_node.next_node
                start_node.next_node = swap_node
            else:
                # 不相邻
                swap_node_a = start_node.next_node
                swap_node_b = parent_node.next_node

                swap_node_b.next_node, swap_node_a.next_node = swap_node_a.next_node, swap_node_b.next_node

                start_node.next_node = swap_node_b
                parent_node.next_node = swap_node_a

        start_node = start_node.next_node

    link.head_node = head_node.next_node
    return link


@measure
def selection_sort_swap_value(link: Link) -> Link:
    """
    选择排序

    不交换节点，只交换值的方式
    """
    head_node = Node(0, link.head_node)
    start_node = head_node.next_node
    while start_node:
        swap_node = None
        current_node = start_node.next_node
        while current_node:
            if current_node < start_node:
                if not swap_node or swap_node > current_node:
                    swap_node = current_node

            current_node = current_node.next_node

        if swap_node:
            swap_node.element, start_node.element = start_node.element, swap_node.element

        start_node = start_node.next_node

    link.head_node = head_node.next_node
    return link


@measure
def quicksort_main(link: Link) -> Link:
    """
    快速排序（递归）

    测试:
        链表的长度为 1000 --- Total execution time: 11 ms
        链表的长度为 10000 --- Total execution time: 143 ms

    问题:
        1. 链表太长时，递归深度太大，影响性能

    优化:
        1. 不使用递归的方式
    """
    if link.head_node and link.head_node.next_node:
        quicksort(link.head_node, Node)
    return link


def quicksort(head_node: Node, tail_node: Node):
    """
    快速排序（递归）

    说明：
        右链表右边界使用闭区间，左链表的左边界使用开区间
    """
    if head_node and head_node != tail_node and head_node.next_node != tail_node:
        middle_node = partition(head_node, tail_node)
        quicksort(head_node, middle_node)
        quicksort(middle_node.next_node, tail_node)


def partition(start_node: Node, end_node: Node) -> Node:
    """
    将这段链表进行分区

    使用交换值的方式
    :return: 这段链表的中间节点
    """
    # 取最开头的节点为中心点
    pivot = start_node.element

    # 计算中间节点的位置
    middle_node = start_node

    current_node = start_node.next_node
    while current_node and current_node != end_node:
        if current_node.element < pivot:
            middle_node = middle_node.next_node
            current_node.element, middle_node.element = middle_node.element, current_node.element

        current_node = current_node.next_node
    start_node.element, middle_node.element = middle_node.element, start_node.element
    return middle_node


@measure
def quicksort_main_swap_node(link: Link) -> Link:
    """
    快速排序（递归，交换节点）

    测试:
        链表的长度为 1000 --- Total execution time: 19 ms
        链表的长度为 10000 --- Total execution time: 239 ms
    """
    head_pre_node = Node(0, link.head_node)
    quicksort_swap_node(head_pre_node, link.head_node, None)
    link.head_node = head_pre_node.next_node
    return link


def quicksort_swap_node(head_pre_node: Node, head_node: Node, tail_node: Node):
    """
    快速排序（递归，交换节点）

    说明:
        除了需要传入头节点，还需要
        第一次递归的时候，head_node 可能已经不在表头了

    :param head_pre_node: 头节点的父节点
    :head_node: 头节点
    :tail_node: 尾节点
    """
    if head_node and head_node != tail_node and head_node.next_node != tail_node:
        middle_node = partition_swap_node(head_pre_node, head_node, tail_node)
        # 可能 head_node 不在指向表头了
        quicksort_swap_node(head_pre_node, head_pre_node.next_node, middle_node)
        quicksort_swap_node(middle_node, middle_node.next_node, tail_node)


def partition_swap_node(start_pre_node: Node, start_node: Node, end_node: Node) -> Node:
    """
    将这段链表进行分区（交换节点的方式）

    说明：
        范围是左闭右开[start_node, end_node)

    :param start_pre_node: 开始节点的父节点
    :param start_node: 开始节点
    :param end_node: 结束节点
    """
    little_head_node, big_head_node = Node(0), Node(0)
    little_node, big_node = little_head_node, big_head_node
    current_node = start_node.next_node
    while current_node and current_node != end_node:
        if current_node < start_node:
            little_node.next_node = current_node
            little_node = current_node
        else:
            big_node.next_node = current_node
            big_node = current_node

        current_node = current_node.next_node

    little_node.next_node = start_node
    big_node.next_node = end_node
    start_node.next_node = big_head_node.next_node
    start_pre_node.next_node = little_head_node.next_node

    return start_node


@measure
def quicksort_no_recursion(link: Link) -> Link:
    """
    快速排序（非递归）

    说明：
        partition 算法使用交换值的方式

    测试:
        链表的长度为 1000 --- Total execution time: 12 ms
        链表的长度为 10000 --- Total execution time: 145 ms
    """
    temp_nodes = list()
    temp_nodes.extend([link.head_node, Node])
    while temp_nodes:
        end_node = temp_nodes.pop()
        start_node = temp_nodes.pop()
        if start_node and start_node != end_node and start_node.next_node != end_node:
            middle_node = partition(start_node, end_node)
            temp_nodes.extend([start_node, middle_node])
            temp_nodes.extend([middle_node.next_node, end_node])

    return link


if __name__ == "__main__":
    link = init_link(10000, True)
    # print(link)
    # link = insertion_sorting(link)
    link = quicksort_no_recursion(link)
    # print(link)
