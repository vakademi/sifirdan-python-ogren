# Fizz Buzz Testi
# 3'e tam bolunebilenler Fizz
# 5'e tam bolunebilenler Buzz
# 3'e ve 5'e bolunebilenler ise FizzBuzz

# 1-den 100'e kadar sayilar var, bu sayilar Fizz mi Buzz mu yoksa FizzBuzz'mi

for number in range(100):
    fizz_buzz = ""
    if number % 3 == 0:
        fizz_buzz += "Fizz"
    if number % 5 == 0:
        fizz_buzz += "Buzz"
    print(f"{number} {fizz_buzz}")
