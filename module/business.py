#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 07/28/21 11:04:56
# @File   : business.py

import sys
import time

import requests
from tqdm import tqdm

from module import my_crypto
from module import decorator
from models import private_data_model
from models import public_data_model


class Business(object):
    """
    业务逻辑代码
    """

    @decorator.Decrator.authentication
    def __new__(cls) -> 'Business':
        """实例化时，进行鉴权

        Returns:
            Business: 返回Business的实例
        """
        inst = object.__new__(cls)
        return inst

    @decorator.Decrator.authentication
    def __init__(self) -> None:
        """初始化实例时，进行鉴权(实例化鉴权可省略)
        """
        self.data = private_data_model.DataModel()

        self.data.secret['url'] = {
            'search': 'https://smartbox.gtimg.cn/s3',
            'get_data': 'http://qt.gtimg.cn'
        }
        self.data.secret['ciphertext'] = 'Z+fkxFFIRVXq8JXIV62esA=='
        self.data.secret['key'] = '+iZ+17kxM3HS/s8g9Nyr4g=='
        self.data.secret['iv'] = 'mNPogOSSY79BRifl2T1S7g=='

    @staticmethod
    def authentication() -> int:
        """账户鉴权

        Returns:
            int: 鉴权结果, 0表示鉴权成功
        """

        while True:
            input_key = input(f"请输入账户: {public_data_model.DataModel.account} 的密钥: (输入 'exit' 退出程序)\n> ")
            if input_key == 'exit':
                sys.exit()
            elif my_crypto.MyCrypto.compare(input_key, public_data_model.DataModel.account):
                public_data_model.DataModel.input_dict['authentication'] = input_key
                return 0
            else:
                print('校验错误!')
                continue

    @decorator.Decrator.authentication
    def level_1(self) -> str:
        """模块选择

        Returns:
            str: 将要跳转的下一级名称
        """
        while True:
            input_str = input(f"请输入模块对应的代码: (全部:all, 沪深:gp, 港股:hk, 基金:jj, 美股:us, 期货:qh)(输入 'exit' 退出程序)\n> ")
            if input_str == 'exit':
                sys.exit()
            elif input_str in ['all', 'gp', 'hk', 'jj', 'us', 'qh']:
                public_data_model.DataModel.input_dict['level_1'] = input_str
                return 'level_2'
            elif input_str.strip() == '':
                print('输入错误, 请重新输入!')
                continue
            else:
                print('输入错误, 请重新输入!')
                continue
            
    @decorator.Decrator.authentication
    def level_2(self) -> str:
        """关键字搜索

        Returns:
            str: 将要跳转的下一级名称
        """
        while True:
            input_str = input(f"请输入搜索关键字: (输入 'q' 返回上一级)(输入 'exit' 退出程序)\n> ")
            if input_str == 'q':
                public_data_model.DataModel.input_dict['level_2'] = input_str
                return 'level_1'
            elif input_str == 'exit':
                sys.exit()
            elif input_str.strip() == '':
                print('输入错误, 请重新输入!')
                continue
            else:
                public_data_model.DataModel.input_dict['level_2'] = input_str
                plaintext = my_crypto.MyCrypto.decrypto(ciphertext=self.data.secret['ciphertext'], key=self.data.secret['key'], iv=self.data.secret['iv'])
                print(plaintext)
                params = {
                    'v':'2',
                    'q':input_str,
                    't':public_data_model.DataModel.input_dict['level_1']
                }
                response = requests.get(self.data.secret['url']['search'], params=params).text
                response = response.lstrip('v_hint="')
                if response == 'N";':
                    print('未找到!')
                    continue
                for item in response.split('^'):
                    code = f"{item.split('~')[0]}{item.split('~')[1].upper().split('.')[0]}"
                    name = item.split('~')[2].encode('utf-8').decode('unicode_escape')
                    self.data.company_dict[code] = name
                    print(f"{code}: {name}")
                return 'level_3'

    @decorator.Decrator.authentication
    def level_3(self) -> str:
        """根据公司编码选择公司

        Returns:
            str: 将要跳转的下一级名称
        """
        while True:
            input_str = input(f"请输入公司编码: (输入 'q' 返回上一级)(输入 'exit' 退出程序)\n> ")
            if input_str == 'q':
                public_data_model.DataModel.input_dict['level_3'] = input_str
                return 'level_2'
            elif input_str == 'exit':
                sys.exit()
            elif input_str.strip() == '':
                print('输入错误, 请重新输入!')
                continue
            else:
                if input_str in self.data.company_dict.keys():
                    public_data_model.DataModel.input_dict['level_3'] = input_str
                    return 'level_4'
                else:
                    print('编码不在搜索结果中, 请重新输入!')

    @decorator.Decrator.authentication
    def level_4(self) -> str:
        """确认获取次数

        Returns:
            str: 将要跳转的下一级名称
        """
        while True:
            input_str = input(f"请输入次数: (输入 'q' 返回上一级)(输入 'exit' 退出程序)\n> ")
            if input_str == 'q':
                public_data_model.DataModel.input_dict['level_4'] = input_str
                return 'level_3'
            elif input_str == 'exit':
                sys.exit()
            elif input_str.isdigit():
                public_data_model.DataModel.input_dict['level_4'] = input_str
                company_code = public_data_model.DataModel.input_dict['level_3']
                plaintext = my_crypto.MyCrypto.decrypto(ciphertext=self.data.secret['ciphertext'], key=self.data.secret['key'], iv=self.data.secret['iv'])
                print(plaintext)
                # 阅读量+n
                for _ in tqdm(range(int(input_str))):
                    response = requests.get(f"{self.data.secret['url']['get_data']}/q=s_{company_code}").text
                    if response == 'v_pv_none_match="1";':
                        break
                    data = response.split('="')[1].split('~')
                    print(f'交易所: {data[0]}\n股票名字: {data[1]}\n股票代码: {data[2]}\n当前价格: {data[3]}\n涨跌: {data[4]}\n涨跌%: {data[5]}\n成交量: {data[6]}\n成交额: {data[7]}\n总市值: {data[8]}')
                    time.sleep(1)
                if response == 'v_pv_none_match="1";':
                    print('获取失败')
                    continue
                # 更新当前阅读量
                print
            elif input_str.strip() == '':
                print('输入错误, 请重新输入!')
                continue
            else:
                print('输入错误, 请重新输入!')
                continue
