# 아래 함수를 수정하시오.
def get_value_from_dict(dict_1, dict_key):
    result = dict_1.get(dict_key)
    return result


my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice
