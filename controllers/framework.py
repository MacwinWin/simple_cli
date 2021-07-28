#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 07/28/21 11:05:18
# @File   : framework.py

from module import my_crypto
from module import business
from models import public_data_model


def run():
    """框架代码
    """
    # 生成临时账户
    account = my_crypto.MyCrypto.gen_account()
    public_data_model.DataModel.account = account
    while True:
        # 身份校验
        status = business.Business.authentication()
        # 校验通过
        if status == 0:
            next_level = 'level_1'
            business_instance = business.Business()
            while True:
                if next_level == 'authentication':
                    break
                elif next_level == 'level_1':
                    next_level = business_instance.level_1()
                elif next_level == 'level_2':
                    next_level = business_instance.level_2()
                    if next_level == 'level_1':
                        continue
                elif next_level == 'level_3':
                    next_level = business_instance.level_3()
                    if next_level == 'level_2':
                        continue
                elif next_level == 'level_4':
                    next_level = business_instance.level_4()
