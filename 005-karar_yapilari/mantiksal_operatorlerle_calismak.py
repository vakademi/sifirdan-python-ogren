# Ve Operatörü
sys_user_name = "hakanyalcinkaya"
sys_user_password = "1234"
"""
user_name = input("Kullanıcı Adınız: ")
password = input("Şifreniz: ")

if sys_user_name == user_name and sys_user_password == password:
    print("Hoşgeldiniz")
else:
    print("Yanlış Bilgi Girdiniz, Bilgilerinizi Kontrol Ediniz")
"""
# Or Operatörü
"""
gender = input("Cinsiyet Giriniz (Erkek, Kadın)")
if gender == "Erkek" or gender == "Kadın":
    print("Doğru Bilgi Girdiniz")
else:
    print("Yanlış Bilgi Girdiniz")
"""

# Mantıksal operatörlerde öncelik
# Eğer cebimdeki nakit ürünü almak için yeterliyse
# veya
# Kredi kartımdaki limit yeterliyse ve pin bilgisini doğru girmişsem
"""
cash = 600
cc = 500
product = 400
pin = 1234

user_pin = int(input("Kredi Kartı Pin Giriniz: "))
if cash >= product or cc > product and pin == user_pin:
    print("Ürünü alabilirsiniz")
else:
    print("Bilgiler yanlış veya ürün için yeterli paran yok")

"""

# Not
user_name = input("Kullanıcı Adınız: ")

if not user_name:
    print("Kullanıcı Adını Girmediniz")

if not len(user_name) > 0:
    print("Kullanıcı Adını Girmediniz")

if len(user_name) == 0:
    print("Kullanıcı Adını Girmediniz")

if user_name == "":
    print("Kullanıcı Adını Girmediniz")

if not len(user_name) != 0:
    print("Kullanıcı Adını Girmediniz not")
