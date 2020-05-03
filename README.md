# [my-algorithm-exercises](https://github.com/zh826256645/my-algorithm-exercises)
![language](https://img.shields.io/badge/language-python-blue.svg)

深入了解数据结构和算法练习
****
## 运行
1. 本代码在 python3.7 的环境下进行编写

2. 执行代码前请将本项目的根目录加入 `PYTHONPATH` 中, 例如项目在根目录下 `/my-algorithm-exercises`
    ```shell script
    export PYTHONPATH=$PYTHONPATH:/my-algorithm-exercises
    ```
    如果是在 vscode 下进行调试，可以在调试文件中加入如下配置
    ```
    "env": {
        "PYTHONPATH": "$PYTHONPATH:${workspaceRoot}"
    }
    ```

## 项目
1. [链表](https://github.com/zh826256645/my-algorithm-exercises/blob/master/model/link.py)
    - [x] [计算环的长度](https://github.com/zh826256645/my-algorithm-exercises/blob/b43234d586074a9da4a432893b38d1729c157b1d/exercises/link/link.py#L62)
    - [x] [插入排序](https://github.com/zh826256645/my-algorithm-exercises/blob/b43234d586074a9da4a432893b38d1729c157b1d/exercises/link/link_sort.py#L74)
    - [x] [选择排序](https://github.com/zh826256645/my-algorithm-exercises/blob/b43234d586074a9da4a432893b38d1729c157b1d/exercises/link/link_sort.py#L109)
    - [x] [快速排序(递归方式)](https://github.com/zh826256645/my-algorithm-exercises/blob/3001a7da3118ab82dd7ab73329a1a3f29f9e9579/exercises/link/link_sort.py#L187)
    - [x] [快速排序(非递归方式)](https://github.com/zh826256645/my-algorithm-exercises/blob/e9b81e2b87be5e9154a47e6c72fa45345d43f7d3/exercises/link/link_sort.py#L310)
    - [x] [归并排序(递归方式)](https://github.com/zh826256645/my-algorithm-exercises/blob/5bdce20ec3cef25ef97b2157d09e1fe50b998dc3/exercises/link/link_sort.py#L335)
    - [x] 归并排序(非递归方式)