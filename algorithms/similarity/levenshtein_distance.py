# -*- encoding: utf-8 -*-
"""
莱文斯坦距离

@File    :   levenshtein_distance.py
@Time    :   2020/08/18 11:56:46
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   用于计算两个字符串的相似度
"""


class LevenshteinDistance:

    @staticmethod
    def levenshtein(str_1, str_2):
        len_1, len_2 = len(str_1), len(str_2)
        # 初始化二维数组
        table = [[0 for j in range(len_2 + 1)] for i in range(len_1 + 1)]

        # 给行为0或者列为0的单元格赋值
        for i in range(len_1 + 1):
            table[i][0] = i
        for j in range(len_2 + 1):
            table[0][j] = j

        # 根据两个字符是否一样，计算每个单元格的值
        temp = 0
        for i in range(1, len_1 + 1):
            for j in range(1, len_2 + 1):
                if str_1[i-1] == str_2[j-1]:
                    temp = 0
                else:
                    temp = 1

                table[i][j] = min(table[i-1][j-1] + temp, table[i-1][j] + 1, table[i][j-1] + 1)

        # print('\n'.join([str(i) for i in table]))
        # 计算出相似率
        return 1 - table[len_1][len_2] / max(len_1, len_2)


def main():
    str_1 = '听说马上就要放假了'
    str_2 = '你听说要放假了'
    print(LevenshteinDistance.levenshtein(str_1, str_2))


if __name__ == "__main__":
    main()
