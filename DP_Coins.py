#!/bin/python

import sys


def make_change(coins, n):
    solution = [0]*(n+1)
    solution[0] = 1
    for coin in coins:
        for i in range(n+1):
            if i-coin >=0:
                solution[i] += solution[i-coin]
    return solution[i]


n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
coins = map(int, raw_input().strip().split(' '))
print make_change(coins, n)
