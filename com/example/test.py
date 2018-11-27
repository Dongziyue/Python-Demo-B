#!/usr/bin/evn python
# -*- coding: UTF-8 -*-

""" a test module """

__author__ = 'Tom'

import sys


def _fn_private():
    print('this is a private function... 你好')


def fn_test():
    """ test function... """
    print(sys.argv)
    _fn_private()


if __name__ == '__main__':
    fn_test()

print(__name__)
