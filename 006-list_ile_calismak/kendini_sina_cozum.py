invitation_list = [
    "Hakan Yalçınkaya",
    "Ercan Bozkurt",
    "Graham Chapman",
    "John Cleese",
    "Terry Gilliam",
    "Eric Idle",
    "Terry Jones",
    "Michael Palin",
]
# Davetli listesi olsun, input ile isim sor
# Eğer varsa girebilirsiniz desin

name = input("Adınızı Giriniz : ")

if name in invitation_list:
    print("girebilirsiniz")
else:
    print("giremezsiniz")
