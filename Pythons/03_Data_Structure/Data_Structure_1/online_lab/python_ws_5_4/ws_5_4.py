# 아래 함수를 수정하시오.
def capitalize_words(str_lower):
    str_split = str_lower.split()
    str_cap = []
    for i in str_split:
        str_cap.append(i.capitalize())
    return ' '.join(str_cap)


result = capitalize_words("hello, world!")
print(result)
