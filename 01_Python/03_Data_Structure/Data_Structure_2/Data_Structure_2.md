# 7월 23일 수업 내용 정리
## 비시퀀스 데이터 구조
### 딕셔너리
- D.clear() : 딕셔너리의 모든 키/값 쌍을 제거
- D.get(k) : 키 k에 연결된 값을 **반환**(키가 없으면 None을 반환)
- D.get(k, v) : 키 k에 연결된 값을 **반환**하거나 키가 없으면 기본 값으로 v를 반환
- D.keys() : 딕셔너리의 키를 모은 객체를 **반환**
- D.values() : 딕셔너리의 값을 모은 객체를 **반환**
- D.items() : 딕셔너리의 키/값 쌍을 모은 객체를 **반환**
- D.pop() : 딕셔너리에서 키 k를 제거하고 연결됐던 값을 **반환**(없으면 오류)
- D.pop(k, v) : 딕셔너리에서 키 k를 제거하고 연결됐던 값을 **반환**(없으면 v 반환)
- D.setdefault(k) : 딕셔너리에서 키 k와 연결된 값을 **반환**
- D.setdefault(k, v) : 딕셔너리에서 키 k와 연결된 값을 **반환**(k가 딕셔너리의 키가 아니면 값 v와 연결한 키 k를 딕셔너리에 추가하고 v를 반환)
- D.update(other) : other 내 각 키에 대해 딕셔너리에 있는 키면 딕셔너리에 있는 그 키의 값을 other에 있는 값으로 대체, other에 있는 각 키에 대해 딕셔너리에 없는 키면 키/값 쌍을 딕셔너리에 추가

### 세트
- s.add(x) : 세트에 항목 x를 추가, 이미 있다면 변화 없음
- s.clear() : 세트의 모든 항목을 제거(set()가 된다)
- s.remove(x) : 세트에서 항목 x를 제거, 항목 x가 없을 경우 KeyError
- s.pop() : 세트에서 임의의 항목을 **반환**하고, 해당 항목을 제거
- s.discard(x) : 세트에서 항목 x를 제거(remove와 달리 에러 없음)
- s.update(iterable) : 세트에 다른 iterable 요소 추가
![alt text](/python/images/image2.png)

## 참고
### 해시 테이블
### python 문법 규격
- BNF(Backus-Naur Form) : 프로그래밍 언어의 문법을 표현하기 위한 표기법
- EBNF(Extended Backus-Naur Form) : BNF를 확장한 표기법, 메타 기호를 추가하여 더 간결하고 표현력이 강해진 상태
![alt text](/python/images/image3.png)
- BNF와 같은 표기법을 사용하는 이유
    - 서로 다른 프로그래밍 언어, 데이터 형식, 프로토콜 등의 문법을 통일하여 정의하기 위함





.get()은 키에 연결된 값이 없어도 반환 값을 받을 수 있다
dict[key]는 없으면 key error가 난다.

.setdefault = get + alpha
빈 set를 만드려면 b = set()로 만들어야 한다.

해시 함수는 파이썬을 재실행하면 갱신
해시 테이블은 순서가 있다
임의의 크기를 가진 데이터 : key
고전된 크기의 고유한 값 : index
해시 값은 정수로 표현
해시 테이블에 배치된 순서대로 출력

자료구조에서 반드시 할 줄 알아야 하는 것 : CRUD

set : 주머니안에 섞여있는 것

자료 구조, pop(), 반복문을 배웠으니 우리 반 자리 배치

99번 파일먼저