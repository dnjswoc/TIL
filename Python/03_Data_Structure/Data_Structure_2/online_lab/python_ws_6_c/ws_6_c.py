data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
for i in range(len(data)):
    for j in key_list:
        data[i].setdefault(j, 'unknown')
    data_name = data[i].get('name')
    data_company = data[i].get('comapny')
    data_is_collapsible = data[i].get('is_collapsible')
    print(f'{key_list[0]}은/는 {data_name}입니다')
    print(f'{key_list[1]}은/는 {data_company}입니다')
    print(f'{key_list[2]}은/는 {data_is_collapsible}입니다')
    print()