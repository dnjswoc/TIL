list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_book = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]
missing_book = []
# count_t=0
# count=0
# count_m=0
# for rental in rental_book:
#     for number in range(len(list_of_book)):
#         if rental == list_of_book[number]:
#             count+=1
#     count_t+=1
#     if count!=count_t-count_m:
#         count_m+=1
#         print(f'{rental} 을/를 보유하고 있지 않습니다.')
    
# if count == count_t:
#     print(f'모든 도서가 대여 가능한 상태입니다.')

missing_book = [book for book in rental_book if book not in list_of_book]
for book in missing_book:
    print(f'{book} 을/를 보충하여야 합니다.')
if len(missing_book) == 0:
    print('모든 도서가 대여 가능한 상태입니다.')
