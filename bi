#!/usr/bin/env python3

import colors as c
import time

sleep = 1
n = 0

while True:
    for n in range(9001):
        binform = c.clear + c.yellow + '{}: {:04b}' + c.reset
        print(binform.format(n,n))
        time.sleep(sleep)
