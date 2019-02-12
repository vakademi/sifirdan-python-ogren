# if nasıl yazılır ve yazım kuralları nelerdir?
# Eğer kullanıcı adı varsa sistemdeki kullanıcı adıyla eşitse

"""
sys_user_name = "hakanyalcinkaya"
age = int(input("Yaşınızı Giriniz:"))
user_name = input("Kullanıcı Adını Giriniz:")
"Yaşlı", "Orta Yaşlı", "Genç", "Çocuk"
"""

# Eğer sys_username == username'e eşit ise(:)
# Print ile doğru kullanıcı adı girdiniz
"""
sys_user_name = "hakanyalcinkaya"
user_name = input("Kullanıcı Adını Giriniz:")
print(sys_user_name == user_name)

if sys_user_name == user_name:
    print("doğru kullanıcı adı girdiniz")

"""
# Eğer kullanıcı 18 yaşından büyükse
# ekrana sisteme giriş yapabilirsiniz yazdır


"""
age = int(input("Yaşınızı Giriniz :"))

if age > 18:  # if age >= 18
    print("giriş yapabilirsiniz")
"""

# if else nasıl kullanılır?
# Eğer kullanıcı 18 yaşından büyükse
# ekrana  sisteme giriş yapabilirsiniz yazdır
# değilse
# ekrana sisteme giriş yapamazsınız yazdır
"""
age = int(input("Yaşınızı Giriniz :"))
if age > 18:
    print("giriş yapabilirsiniz")
else:
    print("sisteme giriş yapamazsınız")
"""
# if elif else nasıl kullanılır?
# "Yaşlı > 50", "Orta Yaşlı > 30", "Genç > 18", "Çocuk"

age = int(input("Yaşınızı Giriniz :"))
if age >= 0:
    if age > 50:
        print("Maalesef Yaşlısın")
    elif age > 30:
        print("Orta Yaşlısın")
    elif age > 18:
        print("Şanslısın, gençsin")
    else:
        print("Maalesef Çocuksun")
else:
    print("Yanlış bilgi girdiniz")
