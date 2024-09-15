# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:17:38 2024

@author: Nguyễn Thị Thanh Thùy  
"""
so_chan = [so for so in range(2020, 3839) if so % 2 == 0]


so_chia_het_9 = [so for so in so_chan if so % 9 == 0]

print("\t".join(map(str, so_chia_het_9)))
