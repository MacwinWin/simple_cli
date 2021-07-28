#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 07/28/21 11:05:11
# @File   : private_data_model.py

from module import decorator


class DataModel(object):
    """
    数据模型
    """

    # 临时账户
    account = ''
    # 用户输入字典
    input_dict = {}

    @decorator.Decrator.authentication
    def __new__(cls) -> 'DataModel':
        """实例化时，进行鉴权

        Returns:
            Data: 返回Data的实例
        """
        inst = object.__new__(cls)
        return inst

    @decorator.Decrator.authentication
    def __init__(self) -> None:
        """初始化实例时，进行鉴权(实例化鉴权可省略)
        """
        # 机密数据
        self.__secret = {}

        # 帖子阅读量字典
        self.__company_dict = {}

    @property
    @decorator.Decrator.authentication
    def secret(self):
        return self.__secret

    @property
    @decorator.Decrator.authentication
    def company_dict(self):
        return self.__company_dict

