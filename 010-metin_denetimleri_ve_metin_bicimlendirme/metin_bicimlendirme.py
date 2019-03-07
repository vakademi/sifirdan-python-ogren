# https://pyformat.info/
# https://hakanyalcinkaya.github.io/python/004-python-3-6-formatted-string.html

first_name = "Ercan"
last_name = "Bozkurt"
age = 30

greet_first_sample = "Merhaba Ercan Bozkurt, Yasin 30mus"
greet = "Merhaba" + first_name + " " + \
    last_name + ", Yaşın: " + str(age) + " muş"


print("Merhaba %s %s %d" % (first_name, last_name, age))

print("Merhaba {age} {last_name} {first_name}".format(
    first_name=first_name, last_name=last_name, age=age))

print(f"Merhaba {first_name} {last_name} {age}")

print(f"Merhaba {first_name[0:2]}. {last_name}")
print(f"Yasin iki sene sonra {age + 2} olacak")

info = f"Merhaba {first_name}"
print(info)
first_name = "Hakan"
print(info)
