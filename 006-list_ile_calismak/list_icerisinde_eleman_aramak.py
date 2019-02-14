products = [
    "mouse",
    "mouse_pad",
    "keyboard",
    "harddisk",
    "mouse",
    "monitor",
    "scanner",
    "mouse",
]

# Liste içerisinde istediğimiz eleman kaç adet var ?
list_count = products.count("mouse")   # count
print(list_count)

# Aradığımız liste elemanının index'i nedir?
list_index = products.index("mouse")
print(list_index)

products[list_index] = "degisen eleman"
print(products)

# Liste içerisinde istediğimiz eleman var mı ? True / False
print("mouse" in products)  # True
print("tablet" in products)  # False

if "mouse" in products:
    print("mouse listenizde var")
