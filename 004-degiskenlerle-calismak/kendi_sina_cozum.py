# Ürün adı, fiyatı, vergi oranı ve adet bilgilerini kullanıcıdan alan,
# bu bilgileri kullanarak ödenmesi gereken toplam miktarı hesaplayan
# Hesaplama sonucunda aşağıdaki gibi bir sonucu ekranda görüntüleyen
# Python programını kodlayınız.

# Örnek Çıktı:
# 12 adet Mouse için ödenmesi gereken
# toplam miktar KDV dahil 123 Liradır.


# Bilgileri Topla
# Ürün adı al
urun_adi = input("Ürün adını giriniz:")

# Fiyat al
fiyat = input("Ürün fiyatını giriniz:")
fiyat = float(fiyat)
# Vergi oranını al
vergi_orani = int(input("Vergi oranını giriniz (1-100):"))
# Adet al
adet = int(input("Adet bilgisini giriniz:"))

# Hesapla
# urunun vergi dahil fiyatını hesapla, değişkene aktar
vergili_fiyat = fiyat + (fiyat * vergi_orani / 100)
# vergidahil fiyati adet ile carp değişkene aktar
odenecek_toplam = vergili_fiyat * adet

# Cümle Kur
# 12 adet Mouse için ödenmesi gereken
# toplam miktar KDV dahil 123 Liradır.
cumle = str(adet) + " adet " + urun_adi + \
    " için ödenmesi gereken toplam miktar KDV dahil " + \
    str(odenecek_toplam) + " Liradır."

# Cümleyi Göster
print(cumle)
