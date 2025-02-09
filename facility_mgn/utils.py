#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = 'Ahmad Abdulnasir Shuaib <me@ahmadabdulnasir.com.ng>'
__homepage__ = https://ahmadabdulnasir.com.ng
__copyright__ = 'Copyright (c) 2022, salafi'
__version__ = "0.01t"
"""
from uuid import uuid4
from random import randint as ran
from random import choices
from string import ascii_letters as letters


def genserial():
    '''
    Generate a numeric Serial numbers
    '''
    spam = str(uuid4().int >> 64)
    serial = spam[:8]
    ending = ''.join(choices(letters, k=2))
    return f"{serial}{ending}".upper()


def boot():
    pass

if __name__ == "__main__":
    boot()
