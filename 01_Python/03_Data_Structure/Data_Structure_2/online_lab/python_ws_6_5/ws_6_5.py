# 아래 함수를 수정하시오.
def difference_sets(set_1, set_2):
    set_diff = set_1.difference(set_2)
    return set_diff


result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)
