'''
If advantage was just a +X modifier then what would X be?
This can obviously be worked out analytically based on EV but I'm doing this:

 1) For a sanity check
 2) As a very basic foray into MonteCarlo
'''

import random

d_num = 20
n = 100000
total = 0

for i in range(n):
    d1 = random.randint(1,d_num)
    d2 = random.randint(1,d_num)
    total += max(d1, d2)

print("If advantage was just a +X modifier then X would be {x}".format(x = total/n))