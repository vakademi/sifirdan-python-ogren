# List Nasıl Tanımlanır?
fist_list = [1, 2, 3, 4, ]
print(fist_list)

first_list = [12, 3, 4, 5, 6, 6, ]
print(first_list)

# List Tipini Nasıl Kontrol Edebilirim?
print(type(fist_list))

# List İçerisinde Kaç Eleman Var?
print("List İçerisinde Kaç Eleman Var?")
print(len(first_list))

# List İçerisinde Neler Barındırabiliriz?
other_list = [
    "hakan",  # name
    'ercan',  # name
    1,  # price 1
    2,  # price 2
    True,  # Active User
    False,  # Status
    30.0,
    .0,
    [1, 2, 3, 4],
    (1, 2, 3, 4),
    {"user_name": "hakan", "password": "1234"},
]

print(other_list)
