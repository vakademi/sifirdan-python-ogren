first_name = "ErcAn"
email = "Ercan@vakademi.com.tr"

# Metni büyük harfe çevir
print(first_name.upper())
print(first_name)

print("*" * 30)
# Metni küçük harfe çevir
print(first_name.lower())
first_name_lower = first_name.lower()
print(first_name_lower)
print(first_name)

print("*" * 30)
# Metin uzunluğunu bul
print(len(first_name))

print("*" * 30)
# Metinde karakter / bilgi arama
print(first_name.count('e'))
print(first_name.count('E'))
print(first_name.lower().count('e'))

first_name_2 = "Ilgın"
print(first_name_2.lower().count('ı'))
print(first_name_2.lower())

print("*" * 30)
# Metinde karakter / bilgi değiştirme

print(first_name_2.replace('I','ı'))
print(first_name_2.replace('I','ı').lower().count('ı'))
