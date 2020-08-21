# -*- encoding: utf-8 -*-
"""
Jaro-Winkler 距离

@File    :   jaro_winkler_distance.py
@Time    :   2020/08/19 14:29:51
@Author  :   Zhong Hao
@Version :   1.0
@Contact :   zh826256645@gmail.com
@Desc    :   测量两个序列之间的编辑距离
"""


class JaroWinklerDistance:

    P = 0.1
    MAX_P = 0.25
    MAX_L = 4

    @staticmethod
    def jaro_winkler_distance(str_1, str_2, p=None):
        """jaro-winkler 距离

        Keyword arguments:
        str_1 -- 字符串1
        str_2 -- 字符串2
        Return: 匹配值
        """
        if not str_1 and not str_2:
            return 0

        result = JaroWinklerDistance.matches(str_1, str_2)
        m = result[0]
        if not m:
            return 0

        if not p:
            p = JaroWinklerDistance.P

        j = (m / len(str_1) + m / len(str_2) + (m - result[1]) / m) / 3
        return j + min(p, JaroWinklerDistance.MAX_P) * result[2] * (1 - j)

    @staticmethod
    def jaro_distance(str_1, str_2):
        """jaro 距离

        Keyword arguments:
        str_1 -- 字符串1
        str_2 -- 字符串2
        Return: 匹配值
        """
        if not str_1 and not str_2:
            return 0

        result = JaroWinklerDistance.matches(str_1, str_2)
        m = result[0]
        if not m:
            return 0

        return (m / len(str_1) + m / len(str_2) + (m - result[1]) / m) / 3

    @staticmethod
    def matches(str_1, str_2):
        """返回匹配的字符

        Keyword arguments:
        str_1 -- 字符串1
        str_2 -- 字符串2
        Return: 匹配的字符列表
        """
        if len(str_1) > len(str_2):
            max_str, min_str = str_1, str_2
        else:
            max_str, min_str = str_2, str_1

        # 匹配窗口的大小，对于每一行i，列j只在(i-matched_window,i+matched_window)内移动，
        # 在该范围内遇到相等的字符，表示匹配成功
        matched_window = max(len(max_str) // 2 - 1, 0)
        max_match_flag, min_match_flag = [False for _ in range(len(max_str))], [False for _ in range(len(min_str))]
        matches = 0

        for i in range(len(min_str)):
            min_char = min_str[i]

            # 列元素的搜索：j的变化包括i往前搜索窗口长度和i往后搜索窗口长度。
            for j in range(max(i - matched_window, 0), min(i + matched_window + 1, len(max_str))):
                if not max_match_flag[j] and min_char == max_str[j]:
                    max_match_flag[j] = True
                    min_match_flag[i] = True
                    matches += 1
                    break

        # 求转换次数和相同前缀长度
        transpositions, prefix = 0, 0
        j = 0
        for i in range(len(min_str)):
            if min_match_flag[i]:
                while not max_match_flag[j]:
                    j += 1

                if max_str[j] != min_str[i]:
                    transpositions += 1
                j += 1

        for i in range(len(min_str)):
            if str_1[i] != str_2[i]:
                break
            prefix += 1

        return [matches, transpositions / 2, JaroWinklerDistance.MAX_L if prefix > JaroWinklerDistance.MAX_L else prefix]


def main():
    print(JaroWinklerDistance.jaro_distance('abcdefgh', 'abehc'))
    print(JaroWinklerDistance.jaro_winkler_distance('abcdefgh', 'abehc'))


if __name__ == "__main__":
    main()
