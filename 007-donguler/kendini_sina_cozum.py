# Ad ve Soyad bilgilerinden oluşan bir listemiz var.
# Listede bulunan her kişinin adı ve soyadı yine bir liste olarak tanımlanmış.

users = [
    ['Hakan', 'Yalçınkaya', ],
    ['Ercan', 'Bozkurt', ],
    ['Ayşenur', 'Kara', ],
    ['Yasemin Duru', 'Eryılmaz Güngör', ],
    ['Ilgın', 'İlknur', ],
]

# 1. Liste içindeki tüm kullanıcı isimlerini ve
# soyisimlerini ekrana yazdır

for user in users:
    print(user[0], user[1])

# 2. Kullanıcı adının ilk karakteri, soyadın ilk 3 karakteri
# gözükecek şekilde kalan kısımları yıldızlarla doldurarak
# bilgileri ekranda görüntüleyiniz.
# H**** Yal*******

for user in users:
    print(user[0][0] + "*** " + user[1][:3] + "*****")
    first_name_len = len(user[0]) - 1
    last_name_len = len(user[1]) - 3
    print(
        user[0][0] + ("*" * first_name_len),
        user[1][:3] + ("*" * last_name_len)
    )

# 3. Listede yer alan kişilere birer mail adresi tanımlanacak.
# Mail adresi adın baş harfi, arada nokta işareti
# ve soyadın tamamı @firma.com.tr ile birlestirilerek elde ediliyor.
# mail adresi Türkçe karakter içermemeli

for user in users:
    user_name = (
        user[0][0] + "." + user[1] + "@firma.com.tr"
    ).lower()
    user_name = user_name.replace('ı', 'i')
    user_name = user_name.replace(' ', '.')
    user_name = user_name.replace('ç', 'c')
    user_name = user_name.replace('ğ', 'g')
    user_name = user_name.replace('ü', 'u')
    user_name = user_name.replace('ş', 's')
    user_name = user_name.replace('ö', 'o')
    print(user_name)
