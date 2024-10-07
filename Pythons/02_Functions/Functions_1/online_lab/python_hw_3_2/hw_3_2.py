# 아래 함수를 수정하시오.
def add_numbers(a, b):
    result = a + b
    return result


# 수정한 add_numbers() 함수를 호출하시오.
a = 3
b = 5
result = add_numbers(a, b)
print(f'{a}과 {b}를 인자로 ' + '\033[4m' + '넘긴' + '\033[0m' + f' 경우,\n{result}')