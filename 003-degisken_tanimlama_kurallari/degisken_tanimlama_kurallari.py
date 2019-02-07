# Değişken adında boşluk olmaz
# first name = 'Ercan'
first_name = 'Ercan'
print(first_name)

'''
BONUS BİLGİ
first,name = 'Ercan'
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    first,name = 'Ercan'
ValueError: too many values to unpack (expected 2)
>>> first,name = 'Er'
>>> first
'E'
>>> name
'r'
>>> first,name = 'Ercan','Bozkurt'
>>> first
'Ercan'
>>> name
'Bozkurt'
>>> first = name = 'Hakan'
>>> name
'Hakan'
>>> first
'Hakan'
'''

# Değişken adı rakamla başlayamaz ama rakam içerebilir.
# 1bilgi = 'Su sıvıdır'
bilgi2 = 'Su sıvıdır'
print(bilgi2)

# Değişken adında, yalnızca
# alfanumerik (harf ve rakam) karakterler ve _ kullanılabilir
# , + . ( ) [ ] gibi karakterler kullanılamaz.
# first.name = 'Ahmet'


# def ve if gibi Python dilinde özel anlam içeren anahtar kelimeler
# değişken ismi olarak kullanılamaz
# def = 4
# if = 'deneme'


# str int len gibi fonksiyonlar
# değişken adı olarak kullanılırsa özelliğini kaybeder
'''
str(1)
'1'
>>> str(13)
'13'
>>> str = 'Ercan'
>>> print(str)
Ercan
>>> str(13)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    str(13)
TypeError: 'str' object is not callable
'''

# Dalgınlıkla daha önce değişken olarak kullandığımız ismi
# tekrar tanımlamak hata vermez ama keşke hata verse.
# Bu durum beklenmedik sonuçlara sebebiyet verebilir.
# Sonradan atanan değer eskisinin üzerine yazılır.
# Eski değişkenin değeri değişmiş olur.
'''
x = 5
print(x * 2)

x = 'ARABA'
print(x)

x = x + 1
print(x)
'''


# Değişken isimleri büyük küçük harf duyarlıdır.
'''
firstName = 'Ali'
print(firstname)
'''

# Kültür olarak değişken isimlerinde camelCase kullanılmaz.
# Tüm karakterler küçük harfle yazılır.
# Değişken adı birden fazla kelimeden oluşuyorsa
# kelimeler arasında _ kullanılır.
firstName = 'Ali'
first_name = 'Ali'


# Değişken adı okunduğunda anlaşılır olmalı


# Unicode desteği sayesinde değişken adlarında
# Türkçe ve Japonca karakterler dahil, her şey kullanılabilir.
# Fakat, tavsiye edilmez.
