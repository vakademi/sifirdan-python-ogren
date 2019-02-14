products = [
    "mouse",
    "mouse_pad",
    "keyboard",
    "harddisk",
    "monitor",
    "scanner",
]

# list elemanlarına nasıl erişirim?
print(products)
print(
    products[1]
)
# elemanlar 0'dan başlar..
print(
    products[0]  # 1. eleman, 0 dan baslar
)
print(products[4])
print(len(products))  # eleman sayisi

print(
    products[len(products) - 1]
)

# list içerisine yeni eleman nasıl eklerim ?
products.append("printer")
print(products)
products.insert(0, "Wireless Keyboard")  # belli bir yere eleman eklemek

# list içerisindeki bir elemanı nasıl düzenlerim ?
products[5] = "web cam"
print(products)

# list içerisinden bir elemanı nasıl çıkarırım ?
removed_item = products.pop(0)
print(products)
print(removed_item)

print(products[0:3])  # 0'dan 3'e kadar olanlari goster
print(products[:3])  # 3 e kadar
print(products[3:])  # 3ten sona kadar
new_list = products[3:]
print(new_list)

print(products[::-1])  # listeyi ters cevirir

print(products[-1])  # son elemana ulasir

print(products[::2])  # step bildirmek 1, 3, 5...

print("hakan yalcinkaya"[:5], "...")
