orders = {
    1: {'keyboard': 10, 'mouse': 20},
    2: {'keyboard': 2, 'mouse': 4},
    3: {'keyboard': 23, 'mouse': 43},
    'product1': {'keyboard': 3, 'mouse': 3},
    'product2': {'keyboard': 4, 'mouse': 41},
}

print(orders.keys())

total_keyboard = 0
for key in orders.keys():
    print(orders[key])
    print(orders[key]['keyboard'])
    total_keyboard += orders[key]['keyboard']

print(total_keyboard)


total_keyboard_value = 0
print(type(orders.values()))
for value in orders.values():
    print(value)
    total_keyboard_value += value['keyboard']

print(total_keyboard_value)

print(orders.items())
for item in orders.items():
    print(item)

new_keyboard_total = 0
for index, value in orders.items():
    print(index)
    print(value)
    new_keyboard_total += value['keyboard']

print(new_keyboard_total)


new_orders = {
    'item1': 20,
    'item2': 10,
    'item3': 5,
}

new_orders_total = 0
for index, value in new_orders.items():
    print(value)
    new_orders_total += value

print(new_orders_total)
