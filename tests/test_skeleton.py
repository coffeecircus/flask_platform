#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from flask_platform.skeleton import fib

__author__ = "DanZhu"
__copyright__ = "DanZhu"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
