my_list = ["ercan", ]
# append()
my_list.append("hakan")
print(my_list)

# extend()
other_list = ["python", "linux", ]
my_list.extend(other_list)
print(my_list)

# insert()
my_list.insert(1, "Visual Studio Code")
print(my_list)

# remove()
print("remove()")
value1 = my_list.remove("hakan")
print(value1)
print(my_list)


# index()
print("index()")
print(my_list.index("python"))


# count()
print("count()")
my_list.append("python")
print(my_list.count("python"))


# pop()
print("pop()")
first_value = my_list.pop(0)
print(first_value)
print(my_list)

# reverse()
print("reverse()")
print(my_list)
my_list.reverse()
print(my_list)

# sort()
numbers = [2, 3, 5, 1, ]
print("sort()")
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# copy()
print("copy()")
print(numbers)

new_numbers = numbers
new_numbers.append(10)
print("new numbers")
print(new_numbers)

print("numbers")
print(numbers)
# listeyi yedekleyip calismak icin copy

copy_list = numbers.copy()
print("copy_list")
print(copy_list)

print("numbers")
print(numbers)

copy_list.append(20)

print("copy_list")
print(copy_list)

print("numbers")
print(numbers)

# clear()
print("clear()")
print(copy_list)
copy_list.clear()
print(copy_list)


# list()
print("list()")
laptop = "laptop"
list_laptop = list(laptop)

print(list_laptop)

# len()
print("len()")
print(len(list_laptop))

# max()
print("max()")
print(numbers)
print(max(numbers))

# min()
print("min()")
print(numbers)
print(min(numbers))

# reversed()
print("reversed()")
print(numbers)
rev = list(reversed(numbers))
print(numbers)
print(rev)

# slice()
print("slice()")
print(numbers)
print(numbers[::2])
cift = slice(0, None, 2)
print(numbers[cift])

# sum()
print("sum()")
print(numbers)
print("sum:", sum(numbers))
