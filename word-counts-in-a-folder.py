#!/usr/bin/env python
# -*- coding: utf-8 -*-

from glob import glob
from collections import Counter
import re
import os

folderpaths = "C:\\o2\\20171204_unity\\oyunBolumleri\\DilPaketleri\\TR\\PACK2"
counter = Counter()

filepaths = glob(os.path.join(folderpaths,'*.txt'))
for file in filepaths:
    with open(file,encoding='utf8') as f:
        words = re.findall(r'\w+', f.read().lower())
        counter = counter + Counter(words)
print(len(counter))