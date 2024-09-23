# 아래 함수를 수정하시오.
def reverse_string(str_before):
    str_after = []
    str_after.extend(str_before)
    str_after.reverse()
    return ''.join(str_after)


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
