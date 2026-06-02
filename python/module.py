import greet
import mathe
greet.greet_func(greet.person1['name'])
a = int(input('enter 1st num:'))
b = int(input('enter 2nd num:'))
print('sum is:',mathe.sum_fun(a,b))
print('sub is:',mathe.sub_fun(a,b))
print('multi is:',mathe.multi_fun(a,b))


import platform
x= dir(platform)
print(x)

import math
print(math.sqrt(16))
print(math.comb(4,2))
print(math.factorial(5))
print(math.acos(1))
print(math.cos(1))
print(math.acos(-1))
print(math.acos(0.55))
print(math.trunc(2.76543))
print(math.ceil(2.346))
print(math.tau)
print(math.pi)

import datetime
x = datetime.datetime.now()
print("datetime: ",x)
print(x.year)
print(x.month)
print(x.day)

import random
cnum = random.randrange(0,100)
print(cnum)
num = random.randint(0,100)
print(num)