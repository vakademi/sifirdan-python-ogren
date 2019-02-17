# 1'den 10'a Kadar Nasıl Yazdırırız?
print("# 1'den 10'a Kadar Nasıl Yazdırırız?")
number = 1

while number != 10:
    print(number)
    # number = number + 1
    number += 1

# 10'dan 1'e Yazdırın
print("# 10'dan 1'e Yazdırın")
number_2 = 10

while number_2 != 0:
    print(number_2)
    # number_2 = number_2 - 1
    number_2 -= 1

# 1'den 10'a Çift Sayılar
print("# 1'den 10'a Çift Sayılar")
number_3 = 1
while number_3 != 10:
    if number_3 % 2 == 0:
        print(number_3)
    number_3 += 1


# Kullanıcıdan değerler almak

name = ""
invitation_list = []
print("Çıkış İçin x Yazıp Enter'a Basabilirsiniz")
while name != "x":
    name = input("Lütfen İsim Giriniz : ")
    if name != "x":
        invitation_list.append(name)
    print(invitation_list)
