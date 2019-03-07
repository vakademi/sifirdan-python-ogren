# Dictionary'e Neden İhtiyaç Vardır?
product_list = ['Kalem', 4, 'Silgi', 2, 'Çanta', 10, ]

products = ['Kalem', 'Silgi', 'Çanta', ]
prices = [4, 2, 10, ]

for item in range(len(products)):
    print(products[item])
    print(prices[item])


# Dictionary Nasıl Tanımlanır ?
# [] -> List
# () -> Tuple
# {} -> Dict

# l = list()
# t = tuple()
# d = dict()

products_dict = {
    'kalem': 4,
    'silgi': 2,
    'çanta': 10,
    1: "Hakan",
    2: ['Python', 'Django'],
    3: {'laptop': 'mac book pro', 'mouse': 'lg mouse'}
}

print(products_dict)

# Dictionary elemanlarına nasıl erişilir?
print(products_dict['kalem'])
print(products_dict[2])
print(type(products_dict))
print(type(products_dict[2]))
print(products_dict[2][1])
