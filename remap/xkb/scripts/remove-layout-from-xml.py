#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import xml.etree.ElementTree as ET

if len(sys.argv) != 3:
    print('remove-layout-from-xml needs exactly 2 argument', file=sys.stderr)
fname = sys.argv[1]
layout = sys.argv[2]

tree = ET.parse(fname)
root = tree.getroot()
layoutList = root.find('layoutList')
layoutList[:] = [layout_xml for layout_xml in layoutList if layout_xml.find('configItem').find('name').text != layout]
layoutList[-1].tail = '\n  '
root.tail = '\n'
tree.write(fname)
