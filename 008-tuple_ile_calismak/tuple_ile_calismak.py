# Tuple nedir? Neden kullanılır?


# Nasıl tanımlanır?
user = (
    'hakanyalcinkaya',
    12345,
    'hakanyalcinkaya@gmail.com',
    1,
    2,
    3,
)

print(user)
print(type(user))


# Elemanlarına nasıl erişirim?
print(user[2])

# Baştan sona tüm elemanlar
print(user)

# Baştan ilk 3 eleman
print(user[:3])

# Sondan 3 eleman
print(user[-3:])

# 3'ten sonraki elemanlar
print(user[3:])

# Nasıl değer eklerim?
# ekleyemezsin :)
# user.append(1)  # hata alirsin

# Değer nasıl değiştirilir?
# user[0] = 'Ercan'  # hata alirsin -> deger degistirilemez

# Tuple'dan nasıl değer silerim?
# silemezsin :)

# For ile nasıl kullanılır?
for item in user:
    print(item)


# icinde 'Python' kelimesi var mi ?

print('hakanyalcinkaya' in user)

if 'hakanyalcinkaya' in user:
    print("Varrr")


# uzunlugu nedir
print(len(user))

# tuple icinde tuple
new_t = (1, 2, 3, 'hakan', 'ercan', (1, 2, 3, 'vakademi'))
print(new_t[5][3])

# tuple icinde list
new_t_list = (['hakan', 'ercan'], 123456)
print(new_t_list[0])
print(new_t_list[1])

# list icinde tuple
new_list_with_tuple = [
    'hakan',
    'ercan',
    ('hakanyalcinkaya@gmail.com', 'ebozkurt@amigadunyasi.com'),
]

new_list_with_tuple[1] = 'bozkurt'
print(new_list_with_tuple)
print(new_list_with_tuple[2])
# new_list_with_tuple[2][0] = 'hakan.yalcinkaya@gmail.com'  # yapamazsın
new_tuple = ('user@user.com', 'user2@user.com')
new_list_with_tuple[2] = new_tuple
print(new_list_with_tuple)


# list ve tuple arasinda convert
new_list = list(new_tuple)
print(new_list)
print(type(new_list))

# index bilgisi nedir?

print(
    new_list_with_tuple[2].index('user2@user.com')
)

print(
    user.index('hakanyalcinkaya@gmail.com')
)
