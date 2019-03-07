new_orders = {
    'item1': 20,
    'item2': 10,
    'item3': 5,
}

# len
print(len(new_orders))

# sum
print(sum(new_orders.values()))

# get
print(new_orders.get('hakan', 'yalcinkaya'))
print(new_orders.get('hakan', ))
print(new_orders.get('item3'))


# pop
item3 = new_orders.pop('item3')
print(item3)
print(new_orders)

# popitem
print('popitem')
print(new_orders)
print(new_orders.popitem())
print(new_orders)

# keys
print('keys')
new_orders['name'] = 'Ercan'
print(new_orders.keys())

# values
print('values')
print(new_orders.values())

# items
print('items')
print(new_orders.items())

# copy
# Kotu Ornek:
"""
new_orders_2 = new_orders
new_orders_2['name'] = 'Hakan'
print(new_orders)
print(new_orders_2)
"""

# Copy Kullanimi:
new_orders_2 = new_orders.copy()
new_orders_2['name'] = 'Hakan'
print(new_orders)
print(new_orders_2)


# clear
new_orders.clear()
print(new_orders)
print(new_orders_2)
