# Atlama İfadeleri Nelerdir?

# Döngüyü terk etmek için break

# Döngünün sadece o turunu tamamlamadan bir sonraki tura devam etmek
# için continue

numbers = [1, 2, 3, 4, 5, 7, 8, 6, 9, ]

# counter = 0
# value = 1
# while counter < len(numbers):
#     if numbers[counter] == value:
#         value += 1
#     else:
#         break
#     counter += 1

# print("value:", value - 1)
# print("counter:", counter)
# print("son duzgun eleman > numbers list:", numbers[counter - 1])


# value = 1
# for counter in range(len(numbers)):
#     if numbers[counter] == value:
#         value += 1
#     else:
#         break

# print("value:", value - 1)
# print("counter:", counter)
# print("son duzgun eleman > numbers list:", numbers[counter - 1])

value = 1
for number in numbers:
    if number == value:
        value += 1
    else:
        break

print("value:", value)
print("number:", number)
print("numbers list:", numbers[value - 1])

text = "He l l o W o rl d"

for char in text:
    if char == ' ' or char == 'o':
        continue
    print(char)
