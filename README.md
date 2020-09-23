# [my-algorithm-exercises](https://github.com/zh826256645/my-algorithm-exercises)
![language](https://img.shields.io/badge/language-python-blue.svg)

深入了解数据结构和算法练习
****
## 运行
1. 项目的所有代码都在 python3.7 的环境下进行编写

2. 执行代码前请将本项目的根目录加入 `PYTHONPATH` 中, 例如项目在根目录下 `/my-algorithm-exercises`
    ```shell script
    export PYTHONPATH=$PYTHONPATH:/my-algorithm-exercises
    ```
    如果在 `VS Code` 下进行调试，可以在调试配置文件中加入如下配置
    ```
    "env": {
        "PYTHONPATH": "$PYTHONPATH:${workspaceRoot}"
    }
    ```

## 项目
1. [单向链表](https://github.com/zh826256645/my-algorithm-exercises/blob/master/model/link.py)
    - [x] [计算环的长度](https://github.com/zh826256645/my-algorithm-exercises/blob/b43234d586074a9da4a432893b38d1729c157b1d/exercises/link/link.py#L62)
    - [x] [冒泡排序](https://github.com/zh826256645/my-algorithm-exercises/blob/26e2d73b4dfd496acf43f63c6cebc16730c4acd7/exercises/link/link_sort.py#L496)
    - [x] [插入排序](https://github.com/zh826256645/my-algorithm-exercises/blob/b43234d586074a9da4a432893b38d1729c157b1d/exercises/link/link_sort.py#L74)
    - [x] [选择排序](https://github.com/zh826256645/my-algorithm-exercises/blob/b43234d586074a9da4a432893b38d1729c157b1d/exercises/link/link_sort.py#L109)
    - [x] [快速排序(递归方式)](https://github.com/zh826256645/my-algorithm-exercises/blob/3001a7da3118ab82dd7ab73329a1a3f29f9e9579/exercises/link/link_sort.py#L187)
    - [x] [快速排序(非递归方式)](https://github.com/zh826256645/my-algorithm-exercises/blob/e9b81e2b87be5e9154a47e6c72fa45345d43f7d3/exercises/link/link_sort.py#L310)
    - [x] [归并排序(递归方式)](https://github.com/zh826256645/my-algorithm-exercises/blob/5bdce20ec3cef25ef97b2157d09e1fe50b998dc3/exercises/link/link_sort.py#L335)
    - [x] [归并排序(非递归方式)](https://github.com/zh826256645/my-algorithm-exercises/blob/ec7f56580d7024fc77044632e98b37cc5b7eb705/exercises/link/link_sort.py#L432)
2. [双向链表](https://github.com/zh826256645/my-algorithm-exercises/blob/master/model/dbl_link.py)
    - [x] [LRU 缓存](https://github.com/zh826256645/my-algorithm-exercises/blob/master/model/lru_cache.py)
3. [二叉树](https://github.com/zh826256645/my-algorithm-exercises/blob/master/model/binary_tree.py)
    - [x] [二叉搜索树](https://github.com/zh826256645/my-algorithm-exercises/blob/522a264a6a3df2bce67cbfaffaa5fae1dd76d518/model/binary_tree.py#L241)
    - [x] [笛卡尔树](https://github.com/zh826256645/my-algorithm-exercises/blob/522a264a6a3df2bce67cbfaffaa5fae1dd76d518/model/binary_tree.py#L191)
    - [x] [IP 树](https://github.com/zh826256645/my-algorithm-exercises/blob/master/model/ip_tree.py)
    - [x] [自平衡二叉搜索树](https://github.com/zh826256645/my-algorithm-exercises/blob/master/model/avl_tree.py)
    - [x] [堆树](https://github.com/zh826256645/my-algorithm-exercises/blob/master/model/treap.py)
    - [x] [伸展树](https://github.com/zh826256645/my-algorithm-exercises/blob/master/model/splay_tree.py)
