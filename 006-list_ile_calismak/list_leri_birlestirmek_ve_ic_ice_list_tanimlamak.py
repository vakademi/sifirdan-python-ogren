supplier1 = ["mac book pro", "iPhone"]
supplier2 = ["canon 5d mark III", "razer blackwidow"]

# List leri nasıl binbmn mnmbm nmbmn mnbmnb mnbm mnb mnbmnb mn mnbb jhfj fgjfh ghfgfhg hgfhfh hgf hgfjhg rleştiririm ?
print("supplier")
supplier = supplier1 + supplier2
print(supplier)
print(len(supplier))

print("supplier - 1")
print(
    supplier1.append(supplier2)  # birlestirme islemi yapmaz
)
print(len(supplier1))
print(supplier1)

print("new_suppliers")
# new_suppliers = ["mac mini"] + supplier1 + supplier2  # birinci yontem
new_suppliers = ["mac mini", *supplier1,  *supplier2]  # ikinci yontem
print(new_suppliers)

""" 
Hatali yontem
print("ercan_supplier")
ercan_supplier = ["mac mini"]
ercan_supplier.append(*supplier2)
print(ercan_supplier)
"""

# İç içe list ler nasıl oluştururum ?
sub_list = [
    [1, 2, 3, 4, ],
    ["ercan", "hakan", "python", ],
    "linux",
    ["0ah-hakan", "01p-ercan", "02l-python", ]
]

print("sub_list")
print(sub_list)
print(len(sub_list))


# sublist icerisindeki python elemanına nasıl erişirim ?

print(sub_list[1][2])
print(sub_list[2][0])
print(sub_list[2][0:3])
print(sub_list[1][2][:3])
print(sub_list[3][2][:3])
