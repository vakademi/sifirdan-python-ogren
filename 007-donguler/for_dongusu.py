# Liste içerisindeki elemanların yazılması
print("Liste içerisindeki elemanların yazılması")
invitation_list = [
    "Hakan",
    "Ercan",
    "Python",
    "Code",
]

for item in invitation_list:
    print(item)

name = "Hakan Yalcinkaya"

for n in name:
    print(n)

# 0'den 10'a kadar for ile yazırmak
print("0'dan 10'a kadar for ile yazdırmak")
print(range(10))

for index_number in range(10):
    print(index_number)

for index_num in range(3):
    print(invitation_list[index_num])

# 50'den 100'e kadar 3'er 3'er sayıların ekrana yazdırılması
print("50'den 100'e kadar 3'er 3'er sayıların ekrana yazdırılması")
for number in range(50, 100, 3):
    print(number)


# listenin elemanlarına indexleriyle erişmek
print("listenin elemanlarına indexleriyle erişmek")

# list_len = len(invitation_list)
# print(list_len)

for item_index in range(len(invitation_list)):
    print(invitation_list[item_index])

for item_key, item_value in enumerate(invitation_list):
    print("item key", item_key)
    print("item value", item_value)

for key, value in enumerate(invitation_list):
    print("item key", key)
    print("item value", value)
