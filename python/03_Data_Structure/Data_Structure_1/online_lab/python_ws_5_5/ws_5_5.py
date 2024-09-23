# 아래 함수를 수정하시오.
def even_elements(num_list):
    even_list = []
    even_list.extend(num_list)
    count=0
    for i in num_list:
        if i%2!=0:
            even_list.pop(count)
            count+=1
    return even_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
