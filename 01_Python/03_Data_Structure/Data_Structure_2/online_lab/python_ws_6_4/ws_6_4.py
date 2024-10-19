# 아래 함수를 수정하시오.
def get_keys_from_dict(dict_1):
    key_list = []
    for i in dict_1.keys():
        key_list.append(i)
    return key_list


my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']
