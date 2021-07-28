#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 07/28/21 11:04:47
# @File   : decorator.py

import functools
from typing import Tuple, Callable

from module import my_crypto
from models import public_data_model

class Decrator:
    """装饰器类
    """

    @staticmethod
    def authentication(func: Callable) -> Callable:
        """鉴权装饰器

        Args:
            func (Callable): 被装饰的函数

        Returns:
            Callable: 装饰后的函数
        """
        @functools.wraps(func)
        def wrapper(*args, **kw) -> Tuple[str, str]:
            """调用被装饰函数前进行鉴权

            Returns:
                (tuple): tuple containing:

                    input_str (str): 用户输入的内容, 如果鉴权失败则返回'-1'
                    next_level (str): 将要跳转的下一级名称
            """
            if my_crypto.MyCrypto.compare(public_data_model.DataModel.input_dict['authentication'], public_data_model.DataModel.account):
                return func(*args, **kw)
            else:
                # 返回身份校验
                print('鉴权失败!')
                if func.__name__ == '__init__':
                    return None
                else:
                    return '-1', 'authentication'
        return wrapper
