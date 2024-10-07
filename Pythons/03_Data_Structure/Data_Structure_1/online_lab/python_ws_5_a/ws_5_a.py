N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.
for i in range(len(data_1)):
    arr_1.append(data_1[i])
print(arr_1)

M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# 아래에 코드를 작성하시오.

arr_2 = data_2.split()
for i in range(len(arr_2)):
    if int(arr_2[i])%2 == 1:
        print(arr_2[i])