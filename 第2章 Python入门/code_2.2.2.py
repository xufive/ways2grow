# -*- encoding: utf-8 -*-

"""
2.2.2 异常捕获与处理
"""

def try_error(n=0):
    try:
        if n == 0:
            raise Warning('这是警告信息')
        if n == 1:
            raise SyntaxError('这是语法错误')
        if n == 2:
            raise IndentationError('这是缩进错误')
        if n == 3:
            raise FileNotFoundError('请求不存在的文件或目录')
    except Warning as e:
        print(e)
    except (SyntaxError, IndentationError) as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    finally:
        print('善后工作')


if __name__ == '__main__':
    try_error()
    try_error(1)
    try_error(2)
    try_error(3)
