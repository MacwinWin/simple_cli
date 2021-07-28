#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 07/28/21 11:04:32
# @File   : main.py

from controllers import framework
from models import public_data_model
from models import private_data_model
from module import business
from module import decorator
from module import my_crypto


if __name__ == '__main__':
    print('当前版本: 1.0')
    print('发布时间: 2021-07-28\n')

    print('----------------------------------------------------\n')

    framework.run()
