# find
text = 'banana'
print(text.find('a'))
print(text.find('z'))

# index
print(text.index('a'))
# print(text.index('z'))

# isupper
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper())  # T
print(string2.isupper())  # F

# islower
print(string1.islower())  # F
print(string2.islower())  # F

# isalpha
string1 = 'Hello'
string2 = '123heis98576ssh'
print(string1.isalpha())  # T
print(string2.isalpha())  # F


# replace
text = 'Hello, world! world world'
new_text = text.replace('world', 'Python', 1)
print(new_text)  # Hello, Python!

# strip
text = '  Hello, world!  '
new_text = text.strip()
print(new_text)

# split
text = 'Hello, world!'
words = text.split(',')
words2 = text.split()
print(words)  # ['Hello', ' world!'] 
print(words2)  # ['Hello,', 'world!'] 


# join
words = ['Hello', 'world!']
new_text = '-'.join(words)
print(new_text)  # Hello-world!

# capitalize
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
print(new_text1)  # Hello, world!

# title
new_text2 = text.title()
print(new_text2)  # Hello, World!

# upper
new_text3 = text.upper()
print(new_text3)  # HELLO, WORLD!

# lower
new_text4 = text.lower()
print(new_text4)  # hello, world!

# swapcase
new_text5 = text.swapcase()
print(new_text5)  # HEllO, WOrLD!


# 참고
# isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
print("isdecimal() 메서드 예시:")
print("'12345'.isdecimal():", '12345'.isdecimal())
print("'123.45'.isdecimal():", '123.45'.isdecimal())
print("'-123'.isdecimal():", '-123'.isdecimal())
print("'Ⅳ'.isdecimal():", 'Ⅳ'.isdecimal())
print("'½'.isdecimal():", '½'.isdecimal())
print("'²'.isdecimal():", '²'.isdecimal())
print()

# isdigit() : 일반 숫자뿐만 아니라 지수 표현(²)도 True로 인식
print("isdigit() 메서드 예시:")
print("'12345'.isdigit():", '12345'.isdigit())
print("'123.45'.isdigit():", '123.45'.isdigit())
print("'-123'.isdigit():", '-123'.isdigit())
print("'Ⅳ'.isdigit():", 'Ⅳ'.isdigit())
print("'½'.isdigit():", '½'.isdigit())
print("'²'.isdigit():", '²'.isdigit())
print()

# isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
print("isnumeric() 메서드 예시:")
print("'12345'.isnumeric():", '12345'.isnumeric())
print("'123.45'.isnumeric():", '123.45'.isnumeric())
print("'-123'.isnumeric():", '-123'.isnumeric())
print("'Ⅳ'.isnumeric():", 'Ⅳ'.isnumeric())
print("'½'.isnumeric():", '½'.isnumeric())
print("'²'.isnumeric():", '²'.isnumeric())
