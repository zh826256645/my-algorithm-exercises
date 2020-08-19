# -*- encoding: utf-8 -*-
"""
汉明距离

@File    :   hamming_distance.py
@Time    :   2020/08/19 09:25:49
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   None
"""


class HammingDistance:

    @staticmethod
    def hamming_distance(str_1, str_2):
        if len(str_1) != len(str_2):
            raise ValueError('Undefined for sequences of unequal length')
        return sum(el_1 != el_2 for el_1, el_2 in zip(str_1, str_2))


def main():
    print(HammingDistance.hamming_distance('dbc', 'abe'))


if __name__ == "__main__":
    main()
