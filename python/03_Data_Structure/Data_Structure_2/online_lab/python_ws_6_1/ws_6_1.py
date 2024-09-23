# 아래 함수를 수정하시오.
def union_sets(set_1, set_2):
    set_un = set_1.union(set_2)
    return set_un


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)
