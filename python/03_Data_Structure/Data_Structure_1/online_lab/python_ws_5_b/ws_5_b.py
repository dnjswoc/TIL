data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
new_data=[]
for i in range(len(data_1)):
    new_data.append(data_1[i])
arr_data = []
for i in range(len(new_data)):
    if (new_data[i].isupper() == True) or (new_data[i] == ' '):
        arr_data.append(new_data[i])
for num in arr_data:
    print(num, end='')

print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.
arr_num = []
arr_num.append(data_2.find('내'))
arr_num.append(data_2.find('힘'))
arr_num.append(data_2.find('들'))
arr_num.append(data_2.find('다'))
print(arr_num)
arr_num.sort(reverse=False)
print(arr_num)
for i in arr_num:
    arr.append(data_2[i])
for num in arr:
    print(num, end='')