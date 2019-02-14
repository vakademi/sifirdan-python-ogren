# String'lerin parçalayıp list nasıl elde ederiz?
names = "hakan, ercan, python"
name_list = names.split(", ")

print(name_list)
print(len(name_list))

# List içerisindeki verilerin birleştirilip
# nasıl tek bir string veri elde ederim?
new_name_list = ['hakan', 'ercan', 'python']
new_names = ", ".join(new_name_list)

print(new_names)
print(type(new_names))
