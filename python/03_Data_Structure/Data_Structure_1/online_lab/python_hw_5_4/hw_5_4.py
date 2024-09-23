# 아래 함수를 수정하시오.
def find_min_max(old_list):
    max_list = max(old_list)
    min_list = min(old_list)
    return min_list, max_list


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
