# https://pyformat.info/
# https://hakanyalcinkaya.github.io/python/004-python-3-6-formatted-string.html


order_no = 103
# istenilen bicim : 0000000103

# 10 haneli > basinda sifirla baslasin

print("0000000"+str(order_no))

digit = 10
zero_count = digit - len(str(order_no))
print(zero_count)

print(("0" * zero_count) + str(order_no))

print(f"{order_no:010}")
print(f"{order_no:0>10}")
print(f"{order_no:0<10}")
print(f"{order_no:0^10}")
print(f"{order_no:*^10}")
