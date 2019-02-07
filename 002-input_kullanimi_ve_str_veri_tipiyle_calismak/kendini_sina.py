# 1. ADIM
# Kullanıcıdan adını, soyadını ve yaşını aldıktan sonra
# aşağıdaki gibi bir cümle kuran programı kodlayınız.
# Örnek Cümle:
# Ercan Bozkurt adlı kişi 39 yaşındadır.

first_name = input("Adınızı giriniz: ")
last_name = input("Soyadınızı giriniz: ")
age = input("Yaşınızı giriniz: ")

print(first_name + " " + last_name + " adlı kişi " + age + " yaşındadır.")

# 2. ADIM
# Hepsi küçük harflerle olacak şekilde
# ad ve soyad bilgilerini kullanarak
# email adresi oluşturup ekranda görüntüleyen
# programı kodlayınız.
# Örnek Adres: ercan.bozkurt@vakademi.com.tr

domain = "@vakademi.com.tr"
email = first_name.lower() + "." + last_name.lower() + domain
print(email)

# 3. ADIM
# Kullanıcıdan alınan ad ve soyad bilgilerinin
# toplam kaç karakterden oluştuğunu
# ekranda görüntüleyen programı kodlayınız.
# Örnek Çıktı: 12

length = len(first_name) + len(last_name)
print(length)
