#!/usr/bin/env python
# -*- coding: utf-8
# pytest unit tests for gifmaker

import os
import imageio

from gifmaker import __path__
from gifmaker.gifmaker import *


def test_creategif():
    """Very basic integrity test that checks if a gif is created, and with proper dimensions."""
    creategif([os.path.join(__path__[0], 'tests/images/1.png'),
               os.path.join(__path__[0], 'tests/images/2.png')],
              'anim.gif', 0.1)
    im = imageio.imread('anim.gif')
    assert im.shape == (1344, 2294, 4)
