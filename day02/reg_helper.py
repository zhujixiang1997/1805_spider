# -*-coding: utf-8 -*-
__author__ = 'zjx'
__data__ = '2018/12/18 0018 10:29'

'''
正则表达式常见的应用场景功能封装
'''
import re


class RegHelper(object):
    def __init__(self, input_str):
        self.__input_str = input_str

    @staticmethod
    def check_card_isvalid(card_str):
        str = re.compile(r"^([1-9]\d{5}[12]\d{3}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])\d{3}[0-9xX])$")
        result = str.match(card_str)
        return False if result == None else True

    @staticmethod
    def check_ip_isvalid(ip_str):
        str = re.compile(r"^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$")
        result = str.match(ip_str)
        return False if result==None else True