# -*- encoding: utf-8 -*-
"""
利用二叉树进行 IP 搜索

@File    :   ip_tree.py
@Time    :   2020/08/24 11:06:39
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   None
"""

from model.binary_tree import BiTNode, BinaryTree


class IPNode(BiTNode):

    def __init__(self, element=None, left=None, right=None, address_code=None) -> None:
        super().__init__(element, left, right)
        self.address_code = address_code


class IPTree(BinaryTree):
    """IP 搜索树

    """

    def __init__(self, root=None) -> None:
        if not root:
            root = IPNode()

        super().__init__(root)
        self.no_address = '未知'

    def train(self, ip_start, ip_end, address_code):
        """将 IP 地址添加到树上

        Keyword arguments:
        ip_start -- IP 起始地址
        ip_end -- IP 结束地址
        address_code -- 地址编码
        """
        ip_s, ip_e = self.ip_to_int(ip_start), self.ip_to_int(ip_end)

        if ip_s == -1 or ip_e == -1:
            return

        current = self.root
        left, right = None, None
        flag = False

        for i in range(32):
            ip_s_bit = (0x80000000 & ip_s) >> 31
            ip_e_bit = (0x80000000 & ip_e) >> 31

            if not flag:
                if (ip_s_bit ^ ip_e_bit) == 0:
                    if ip_s_bit == 1:
                        if not current.right:
                            current.right = IPNode()
                        current = current.right
                    else:
                        if not current.left:
                            current.left = IPNode()
                        current = current.left

                    if i == 31:
                        current.address_code = address_code
                else:
                    flag = True
                    if not current.left:
                        current.left = IPNode()
                    left = current.left

                    if not current.right:
                        current.right = IPNode()

                    right = current.right

                    if i == 31:
                        left.addressCode = address_code
                        right.address_code = address_code
            else:
                if ip_s_bit == 1:
                    if not left.right:
                        left.right = IPNode()
                    left = left.right
                else:
                    if not left.left:
                        left.left = IPNode()
                    if not left.right:
                        left.right = IPNode()
                    left.right.address_code = address_code
                    left = left.left

                if i == 31:
                    left.address_code = address_code

                if ip_e_bit == 1:
                    if not right.right:
                        right.right = IPNode()
                    if not right.left:
                        right.left = IPNode()
                    right.left.address_code = address_code
                    right = right.right
                else:
                    if not right.left:
                        right.left = IPNode()
                    right = right.left

                if i == 31:
                    right.address_code = address_code

            ip_s = ip_s << 1
            ip_e = ip_e << 1

    def find_ip(self, ip: str) -> str:
        """查找 IP 地址对应的地址编码

        Keyword arguments:
        ip -- IP 地址
        Return: 地址编码
        """

        current = self.root

        ip_int = self.ip_to_int(ip)

        if ip_int == -1:
            return self.no_address

        for i in range(32):
            ip_s_bit = (0x80000000 & ip_int) >> 31

            if ip_s_bit == 0:
                current = current.left
            else:
                current = current.right

            if not current:
                return self.no_address

            if current.address_code and current.address_code.strip():
                return current.address_code

            ip_int = ip_int << 1

        return self.no_address

    @staticmethod
    def ip_to_int(ip: str) -> int:
        """IP 地址转 int

        Keyword arguments:
        ip -- IP 地址
        Return: 整形数值
        """
        try:
            octets = ip.split('.')
            ip_int = (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])
            return ip_int
        except Exception:
            return -1


def main():
    ip_s = IPTree.ip_to_int('1.29.56.0')
    print((0x80000000 & ip_s) >> 31)
    ip_e = IPTree.ip_to_int('1.29.59.255')
    print((0x80000000 & ip_e) >> 31)
    print(0 ^ 0)


if __name__ == "__main__":
    main()
