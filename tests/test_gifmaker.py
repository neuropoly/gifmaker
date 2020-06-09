#!/usr/bin/env python
# -*- coding: utf-8
# pytest unit tests for gifmaker

import imageio

from gifmaker.gifmaker import *


def test_creategif():
    """Very basic integrity test that checks if an output gif with proper dimensions is created"""
    creategif(['images/1.png', 'images/2.png'], 'anim.gif', 0.1)
    im = imageio.imread('anim.gif')
    assert im.shape == (1344, 2294, 4)
