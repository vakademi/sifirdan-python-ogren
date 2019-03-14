# import random
from random import randint, choice

SELECTION_LIST = ('t', 'k', 'm')

"""
Yapilacaklar Listesi:

1. random kütüphanesinden uygun olan fonksiyonu yükle
2. listeni hazırla
3. input ile seçimi al
4. python secimini yapsin
5. fonksiyon yazalim
"""
print("Taş, Kağıt, Makas Oyunu")
print("Seçiminizi Yapın")
print("Seçenekler: Taş(t), Kağıt(k), Makas(m)")
user_selection = input("Seçiminiz: ").lower()
# computer_selection = randint(0, len(SELECTION_LIST))
computer_selection = choice(SELECTION_LIST)


def select_winner(user, computer):
    if user == computer:
        func_result = "Berabere"
    elif (user == "t" and computer == "m") \
            or (user == "k" and computer == "t") \
            or (user == "m" and computer == "k"):
        func_result = "Oyuncu kazandı"
    else:
        func_result = "Python kazandı"
    return func_result


if user_selection in SELECTION_LIST:
    # result = select_winner(user=user_selection, computer=computer_selection)
    result = select_winner(user_selection, computer_selection)
else:
    result = "Yanlis girdiniz"

print(result)
print(result.upper())


'''
T T Draw
T K Comp
T M User

K T User
K K Draw
K M Comp

M T Comp
M K User
M M Draw
'''
