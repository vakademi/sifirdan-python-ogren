# Int(Tam Sayılar) Veri Tipinin Tanıtılması
number = 1
number_2 = 100

# Hesaplamalarda Veri Tiplerini Nasıl Kullanıyoruz?

# print(number + number_2)
total = number + number_2
print(total)
print(number + 200)

# Ekrana Sayı: int veri olarak nasıl yazdırırız?
print("toplam sayi: ", total)

# Değişkenin Tipi Gerçekten Int midir?
var_1 = "araba"
var_2 = 15
var_3 = "15"

print(type(var_1))
print(type(var_2))
print(type(var_3))

var_4 = int(var_3)
var_5 = str(var_2)
print(type(var_4))
print(type(var_5))

print("Veri degeri: " + var_5, type(var_5))


print("toplam sayi: " + str(total))

# String veri tipinden Int'e dönüştürürken
# değerin her karakteri rakam olmalıdır

var_6 = "12345hakan"

# Burda hata alacagiz:
print(int(var_6))
