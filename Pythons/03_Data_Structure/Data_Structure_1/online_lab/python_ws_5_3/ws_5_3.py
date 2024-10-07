# 아래 함수를 수정하시오.
def sort_tuple(num_tuple):
    # new_tuple = tuple(sorted(list(num_tuple)))
    new_list = list(num_tuple)
    new_list.sort()
    new_tuple = tuple(new_list)
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
