# -*-coding: utf-8 -*-
__author__ = 'zjx'
__data__ = '2018/12/18 0018 10:36'
from day02.reg_helper import RegHelper


def test_card():
    card_str = '411521199711111234'
    reg_inst = RegHelper(card_str)
    res = reg_inst.check_card_isvalid(card_str)
    print(res)

def test_ip():
    card_str = '1164355115@qq.com'
    reg_inst = RegHelper(card_str)
    res = reg_inst.check_ip_isvalid(card_str)
    print(res)








if __name__ == '__main__':
    test_card()
    test_ip()
