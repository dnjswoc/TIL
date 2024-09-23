food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.

# for list in range(len(food_list)):
#     if food_list[list]['이름'] == '토마토':
#         food_list[list]['종류'] = '과일'
#     elif food_list[list]['이름'] == '자장면':
#         print('자장면엔 고춧가루지')
#     print(f'{food_list[list]["이름"]} 은/는 {food_list[list]["종류"]}(이)다')
# print(food_list)

list=0
while list < len(food_list):
    if food_list[list]['이름'] == '토마토':
        food_list[list]['종류'] = '과일'
    elif food_list[list]['이름'] == '자장면':
        print('자장면엔 고춧가루지')
    print(f'{food_list[list]["이름"]} 은/는 {food_list[list]["종류"]}(이)다')
    list+=1
print(food_list)