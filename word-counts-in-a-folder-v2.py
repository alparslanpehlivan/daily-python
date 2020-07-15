#!/usr/bin/env python
# -*- coding: utf-8 -*-

from glob import glob
from collections import Counter
import re
import os

packet=1
k=0
for packet in range(31):

    folderpaths = "C:\\o2\\20171204_unity\\oyunBolumleri\\DilPaketleri\\TR\\PACK{}".format(packet)
    counter = Counter()

    filepaths = glob(os.path.join(folderpaths,'*.txt'))
    for file in filepaths:
        with open(file,encoding='utf8') as f:
            words = re.findall(r'\w+', f.read().lower())
            counter = counter + Counter(words)
    k=k+len(counter)

print(k)