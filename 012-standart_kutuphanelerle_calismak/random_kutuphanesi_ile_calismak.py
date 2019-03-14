# print(random(1, 10))
# Hata Aldık cünkü daha önce çağırmadık bu modülü

# from random import *  # random modülünün içindeki her şey
# import random  # modulun tamamını çağır

# from random import randint, choice, \
# choices, randrange  # en performanslı yöntem

# birden fazla modülü parantezler içerisinde çağırmak
from random import (
    randint,
    choice,
)

# a = 1
# b = 10
# rnd = random.randint(a, b)

# print(rnd)

# print(random.randint(1, 10))

print(randint(1, 20))

user_list = [
    'hakan',
    'ahmet',
    'mehmet',
    'ercan',
]


print(randint(0, len(user_list)))  # sayi veriyor
print(choice(user_list))  # secilen degeri veriyor
