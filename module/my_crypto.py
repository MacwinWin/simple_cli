#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 07/28/21 11:04:40
# @File   : my_crypto.py

import hashlib
import uuid
from base64 import b64decode

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


class MyCrypto:
    """
    加密、解密
    """

    @staticmethod
    def gen_account() -> str:
        """生成临时账户

        Returns:
            str: 临时账户
        """
        account = uuid.uuid4().hex
        return account

    @staticmethod
    def __encrypt(account: str) -> str:
        """私有方法, 对account进行sha1加密
        
        Args:
            account (str): 临时账户
        
        Returns:
            str: 加盐sha1后的key
        """
        # 加盐
        key = account + 'oaZADXDzb2aY16H3o2aFEA=='
        # 生成密钥
        m = hashlib.sha1()
        m.update(key.encode('utf-8'))
        key = m.hexdigest()
        return key
    
    @classmethod
    def compare(cls, user_key: str, account: str) -> bool:
        """校验用户输入密钥与后端根据account生成的密钥

        Args:
            user_key (str): 用户输入的密钥
            account (str): 临时账户

        Returns:
            bool: 校验结果的布尔值
        """
        # 调用私有方法生成密钥
        key = cls.__encrypt(account)
        # 比较
        if user_key == key:
            return True
        else:
            return False

    def decrypto(ciphertext: str, key: str, iv: str) -> str:
        """根据key和iv, 使用AES算法的CBS模式进行解密

        Args:
            ciphertext (str): 待解密的密文
            key (str): 预留的key
            iv (str): 预留的iv
        
        Returns:
            str: 解密后的明文
        """
        ct = b64decode(ciphertext)
        key_b = b64decode(key)
        iv_b = b64decode(iv)
        cipher = AES.new(key_b, AES.MODE_CBC, iv_b)
        # 解密后的明文数据
        pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
        return pt
