#!/usr/bin/env python
# coding: utf-8


import time
NUMBER = 10000

start = time.time()
import get_primes
print(get_primes.get_primes(NUMBER))
my_time = time.time() - start

print(f'my_time: {my_time}')
