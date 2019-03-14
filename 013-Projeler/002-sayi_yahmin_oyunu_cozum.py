# Sayı Tahmin Oyunu -> Çözüm
# 1 ile 10 Arasinda Bir Sayıyı Bilgisayar Tutuyor ve Biz Tahmin Etmeye Çalışıyoruz

from random import randint

computer = randint(1, 10)

user = 0
counter = 0

while not computer == user:  # computer != user
    user = int(input('Sayı Giriniz: '))
    counter += 1
    if user > computer:
        print("Daha Küçük Bir Sayı Girmelisiniz")
    else:
        print("Daha Büyük Bir Sayı Girmelisiniz")


print(f'Tebrikler :), {counter} denemede bildiniz')
print('Tebrikler :), {} denemede bildiniz'.format(counter))
