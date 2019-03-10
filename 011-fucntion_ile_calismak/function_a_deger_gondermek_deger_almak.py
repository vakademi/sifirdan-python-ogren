def hello_world():
    print("Hello World")


# Function'a Değer Göndermek
"""
name = "Hakan"

def hello_name():
    print(f"Hello {name}")
"""


def hello_name(name=None):
    if name:
        print(f"Hello {name}")
    else:
        print(f"Hello")


hello_name()
hello_name('Hakan')

# Function'dan Değer Almak


def hello_return_name(name=None):
    if name:
        return f"Hello {name}"
    return "Hello"


print("Function'dan Değer Almak")
hello = hello_return_name('Python')
print(hello)


# Function'a Birden Fazla Değer Gönndermek

def perim(width, height):
    return (width + height) * 2


res = perim(3, 5)
print(res)


def draw_rect(w, h, character="*"):
    for row in range(h):
        print(character * w)


draw_rect(10, 4)
print()
draw_rect(10, 4, "+")


# Function'dan Birden Fazla Değer Almak

def get_info(first_name, last_name):
    account = first_name.lower() + last_name.lower()
    email = account + "@domain.com.tr"
    return (account, email)


info = get_info('Ercan', 'Bozkurt')
account, email = get_info('Ercan', 'Bozkurt')

print(info)
print(type(info))
print(email)


def get_info_list(first_name, last_name):
    account = first_name.lower() + last_name.lower()
    email = account + "@domain.com.tr"
    return [account, email]


info = get_info_list('Ercan', 'Bozkurt')
print(type(info))


def get_info_dict(first_name, last_name):
    account = first_name.lower() + last_name.lower()
    email = account + "@domain.com.tr"
    return {'account': account, 'email': email}


info = get_info_dict('Ercan', 'Bozkurt')
print(type(info))


def get_info_(first_name, last_name):
    account = first_name.lower() + last_name.lower()
    email = account + "@domain.com.tr"
    return account, email


info = get_info_('Ercan', 'Bozkurt')
print(type(info))
