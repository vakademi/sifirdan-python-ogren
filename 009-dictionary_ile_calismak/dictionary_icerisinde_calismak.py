products = {
    'laptop': 'Mac Book Pro',
    'mouse': 'Lg Mouse',
    'keyboard': 'Razer Blackwidow',
}
# Dictionary içerisine eleman nasıl eklenir?

print(products['mouse'])
print(products)
# products[0] = 1 list ornegi
products['sound'] = 'creative sound blaster'
print(products)

sound_item = products.get('sounds', 'Philips')
s_item = products.get('sounds')
# sound_item = products['sounds'] # Hata alirsin
print(s_item)
print(sound_item)

if not products.get('bound'):
    # products['sounds'] = 'Sound Vision'
    products['bound'] = 'Sound Vision'

print(products)

# Dictionary içerisine eleman nasıl değiştirilir?
products['mouse'] = "Microsoft Mouse"
print(products)

# Dictionary içerisinden nasıl eleman silinir?
mouse = products.pop('mouse')
print(mouse)
print(products)
print(products.pop('laptop'))
print(products)

# Dictionary elemanlarinin tamami nasil silinir?
# products = {}
# products = dict()
# products.clear()
p2 = products
p2['name'] = "Hakan"

products.clear()
# products = {}
print(products)
print(p2)
