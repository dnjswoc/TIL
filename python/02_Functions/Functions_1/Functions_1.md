# 2024년 7월 17일 수업 내용 정리 - Functions 1

- 함수

    - 함구 구조

- 매개변수와 인자

    - 다양한 인자 종류

- 재귀 함수

- 내장 함수

    - 유용한 내장 함수 map & zip

- 함수와 Scope

    - global 키워드

- Packing & Unpacking

    - Packing
    - Unpacking

- 참고

    - 람다 표현식


## 함수

- 함수(Functions)

    - 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음


- 함수를 사용하는 이유

    - 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지

    - **재사용성**이 높아지고, 코드의 **가독성과 유지보수성** 향상

        ![alt text](./images/image_00.png)


### 함수 구조

![alt text](./images/image_01.png)


- 함수 정의와 호출

    - 함수 정의(정의)

        - 함수 정의는 def 키워드로 시작

        - def 키워드 이후 함수 이름 작성

        - 괄호 안에 매개변수를 정의할 수 있음

        - 매개변수(parameter)는 함수에 전달되는 값을 나타냄

            ```python
            def greet(name):
                """입력된 이름 값에
                인사를 하는 메세지를 만드는 함수
                """
                message = 'Hello, ' + name
                return message

            result = greet('Alice')
            print(result)
            ```


    - 함수 body

        - 콜론(:) 다음에 들여쓰기 된 코드 블록

        - 함수가 실행될 때 수행되는 코드를 정의

            ![alt text](./images/image_02.png)


    - Docstring

        - 함수 body 앞에 선택적으로 작성 가능한 함수 설명서

            ![alt text](./images/image_03.png)


    - 함수 반환 값

        - 함수는 필요한 경우 결과를 반환할 수 있음

        - return 키워드 이후에 반환할 값을 명시

        - return문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환

            ![alt text](./images/image_04.png)


    - 함수 호출

        - 함수를 사용하기 위해서는 호출이 필요

        - 함수의 이름과 소괄호를 활용해 호출

        - 필요한 경우 인자(argument)를 전달해야 함

        - 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수에 대입됨

            ![alt text](./images/image_05.png)


- 함수 호출(function call)

    - 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것
        
        ```python
        function_name(arguments)
        ```



## 매개변수와 인자

|매개변수<br>parameter|인자<br>argument|
|:--:|:--:|
|함수를 정의할 때,<br>함수가 받을 값을 나타내는 변수|함수를 호출할 때,<br>실제로 전달되는 값|
<br>


- 매개변수와 인자 예시

    ```python
    def add_numbers(x, y):  # x와 y는 매개변수(parameter)
        result = x + y
        return result

    
    a = 2
    b = 3
    sum_result = add_numbers(a, b)  # a와 b는 인자(argument)
    print(sum_result)
    ```


### 다양한 인자 종류

1. 위치 인자(Positional Arguments)

    - 함수 호출 시 인자의 위치에 따라 전달되는 인자

    - **위치인자는 함수 호출 시 반드시 값을 전달해야 함**

        ```python
        def greet(name, age):
            print(f'안녕하세요, {name}님! {age}살이시군요.')


        greet('Alice', 25)  # 안녕하세요, Alice님! 25살이시군요.
        ```


2. 기본 인자 값(Default Arguments Values)

    - 함수 정의에서 매개변수에 기본 값을 할당하는 것

    - 함수 호출 시 인자를 전달하지 않으면, 기본 값이 매개변수에 할당됨

        ```python
        def greet(name, age=30):
            print(f'안녕하세요, {name}님! {age}살이시군요.')


        greet('Bob')    # 안녕하세요, Bob님! 30살이시군요.
        greet('Charlie', 40)    # 안녕하세요. Charlie님! 40살이시군요.
        ```


3. 키워드 인자(Keyword Arguments)

    - 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자

    - 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음

    - 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달

    - **단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함**

        ```python
        def greet(name, age):
            print(f'안녕하세요, {name}님! {age}살이시군요.')


        greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
        greet(age=35, 'Dave')   # positional argument follows keyword argument
        ```


4. 임의의 인자 목록(Arbitrary Arguemtn Lists)

    - 정해지지 않은 개수의 인자를 처리하는 인자

    - 함수 정의 시 매개변수 앞에 '*'를 붙여 사용하며, 여러 개의 인자를 tuple로 처리

        ```python
        def calculate_sum(*args):
            print(args)
            total = sum(args)
            print(f'합계: {total}')

        """
        (1, 2, 3)
        합계: 6
        """
        calculate_sum(1, 2, 3)
        ```


5. 임의의 키워드 인자 목록(Arbitrary Keyword Argument Lists)

    - 정해지지 않은 개수의 키워드 인자를 처리하는 인자

    - 함수 정의 시 매개변수 앞에 '**'를 붙여 사용하며, 여러 개의 인자를 dictionary로 묶어 처리

        ```python
        def print_info(**kwargs):
            print(kwargs)


        print_info(name='Eve', age=30)  # {'name': 'Eve', 'age': 30}
        ```


- 함수 인자 권장 작성순서

    - 위치 → 기본 → 가변 → 가변 키워드

    - 호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함

    - **단, 모든 상황에 적용되는 절대적인 규칙은 아니며, 상황에 따라 유연하게 조정될 수 있음**


- 인자의 모든 종류를 적용한 예시

    ```python
    def func(pos1, pos2, default_arg='default', *args, **kwargs):
        print('pos1:', pos1)
        print('pos2:', pos2)
        print('default_arg:', default_arg)
        print('args:', args)
        print('kwargs:', kwargs)

    func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')

    """
    pos1: 1
    pos2: 2
    default_arg: 3
    args: (4, 5, 6)
    kwargs: {'key1': 'value1', 'key2': 'value2'}
    """
    ```


## 재귀 함수

- 재귀 함수

    - 함수 내부에서 자기 자신을 호출하는 함수(ex. 팩토리얼)


- 재귀 함수 예시 - 팩토리얼

    ![alt text](./images/image_06.png)

    - factorial 함수는 자기 자신을 재귀적으로 호출하여 입력된 숫자 n의 팩토리얼을 계산

    - 재귀 호출은 n이 0이 될 때까지 반복되며, 종료 조건을 설정하여 재귀 호출이 멈추도록 함

    - 재귀 호출의 결과를 이용하여 문제를 작은 단위의 문제로 분할하고, 분할된 문제들의 결과를 조합하여 최종 결과를 도출

        ```python
        def factorial(n):
            # 종료 조건 : n이 0이면 1을 반환
            if n == 0:
                return 1
            else:
                # 재귀 호출 : n과 n-1의 팩토리얼을 곱한 결과를 반환
                return n * factorial(n - 1)


        # 팩토리얼 계산 예시
        print(factorial(5)) # 120
        ```


- 재귀 함수 특징

    - 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐

    - 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성



- 재귀 함수를 사용하는 이유

    - 문제의 자연스러운 표현

        - 복잡한 문제를 간결하고 직관적으로 표현 가능


    - 코드 간결성

        - 상황에 따라 반복문보다 알고리즘 코드가 더 간결하고 명확해질 수 있음


    - 수학적 문제 해결

        - 수학적 정의가 재귀적으로 표현되는 경우, 직접적인 구현 가능


- 재귀 함수 활용 시 기억해야 할 것

    1. 종료 조건을 명확히

    2. 반복되는 호출이 종료 조건을 향하도록



## 내장 함수

- 내장 함수(Built-in function)

    - python이 기본적으로 제공하는 함수(별도의 import없이 바로 사용 가능)



- 자주 사용되는 내장 함수 예시

    ```python
    numbers = [1, 2, 3, 4, 5]

    print(len(numbers)) # 5
    print(max(numbers)) # 5
    print(min(numbers)) # 1
    print(sum(numbers)) # 15
    print(sorted(numbers, reverse=True))    # [5, 4, 3, 2, 1]
    ```


### 유용한 내장 함수 map & zip

- map(function, iterable)

    - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환

        ```python
        numbers = [1, 2, 3]
        result = map(str, numbers)

        print(result)   # <map object at 0x000000239C915D760>
        print(list(result)) # ['1', '2', '3']
        ```


- map() 활용

    - SWEA 문제의 input 처럼 문자열 '1 2 3'이 입력 되었을 때 활용 예시

        ```python
        numbers1 = input().split()
        print(numbers1) # ['1', '2', '3']

        numbers2 = list(map(int, input().split()))
        print(numbers2) # [1, 2, 3]
        ```



- zip(*iterables)

    - 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

        ```python
        girls = ['jane', 'ashley']
        boys = ['peter', 'jay']
        pair = zip(girls, boys)

        print(pair) # <zip object at 0x000001C76DE58700>
        print(list(pair))   # [('jane', 'peter'), ('ashley', 'jay')]
        ```


- zip() 활용

    - 여러 개의 리스트를 동시에 조회할 때

        ```python
        kr_scores = [10, 20, 30, 50]
        math_scores = [20, 40, 50, 70]
        en_scores = [40, 20, 30, 50]

        for student_scores in zip(kr_scores,math_scores, en_scores):
            print(student_scores)

        """
        (10, 20, 40)
        (20, 40, 20)
        (30, 50, 30)
        (50, 70, 50)
        """
        ```

    - 여러 개의 리스트를 동시에 조회할 때

        ```python
        scors = [
            [10, 20, 30],
            [40, 50, 39],
            [20, 40, 50],
        ]
        for score in zip(*scores):
            print(score)

        """
        (10, 40, 20)
        (20, 50, 40)
        (30, 39, 50)
        """
        ```



## 함수와 Scope

- Python의 범위(scope)

    - 함수는 코드 내부에 **local scope**를 생성하며, 그 외의 공간인 **global scope**로 구분


- 범위와 변수 관계

    - scope

        - global scope : 코드 어디에서든 참조할 수 있는 공간

        - local scope : 함수가 만든 scope(함수 내부에서만 참조 가능)


    - variable

        - global variable : global scope에 정의된 변수

        - local variable : local scope에 정의된 변수



- Scope 예시

    - num은 local scope에 존재하기 때문에 global scope에서 사용할 수 없음

    - 이는 변수의 **수명주기**와 연관이 있음

        ```python
        def func():
            num = 20
            print('local', num) # local 20


        func()

        print('global', num)    # NameError: name 'num' is not defined
        ```



- 변수 수명주기(lifecycle)

    - 변수의 수명주기는 변수가 선언되는 위치와 scope에 따라 결정됨

    1. built-in scope
        - python이 실행된 이후부터 영원히 유지

    2. global scope
        - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지

    3. local scope
        - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

        

- 이름 검색 규칙(Name Resolution)

    - python에서 사용되는 이름(식별자)들은 특정한 이름공간(namespace)에 저장되어 있음

    - 아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule이라고 부름

        1. Local scope : 지역 범위(현재 작업 중인 범위)

        2. Enclosed scope : 지역 범위 한 단계 위 범위

        3. Global scope : 최상단에 위치한 범위
        
        4. Built-in scope : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)

            ![alt text](./images/image_07.png)

    - **함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음**



- LEGB Rule 예시

    - sum이라는 이름을 global scope에서 사용하게 되면서 기존에 built-in scope에 있던 내장함수 sum을 사용하지 못하게 됨

    - sum을 참조 시 LEGB Rule에 따라 global에서 먼저 찾기 때문

        ```python
        print(sum)  # <built-in function sum>
        print(sum(range(3)))    # 3

        sum = 5

        print(sum)  # 5
        print(sum(range(3)))    # TypeError: 'int' object is not callable
        ```


- LEGB Rule 퀴즈

    ![alt text](./images/image_08.png)




### global 키워드

- `global` 키워드

    - 변수의 스코프를 전역 범위로 지정하기 위해 사용

    - 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용

        ```python
        num = 0 # 전역 변수


        def increment():
            global num  # num울 전역 변수로 선언
            num += 1

        
        print(num)  # 0
        increment()
        print(num)  # 1
        ```


- `global` 키워드 주의사항

    - global 키워드 선언 전에 참조 불가

        ```python
        num = 0

        
        def increment():
            # SytaxError: name 'num' is used prior to global declaration
            print(num)
            global num
            num += 1
        ```


    - 매개변수에는 global 키워드 사용 불가

        ```python
        num = 0


        def increment(num):
            # "num" is assigned before global declaration
            global num
            num += 1
        ```



## Packing & Unpacking

### Packing

- Packing(패킹)

    - 여러 개의 값을 하나의 변수로 묶어서 담는 것


- 패킹 예시

    - 변수에 담긴 값들은 튜플(tuple) 형태로 묶임

        ```python
        packed_values = 1, 2, 3, 4, 5
        print(packed_values)    # (1, 2, 3, 4, 5)
        ```


- '*'을 활용한 패킹

    - *b는 남는 요소들을 리스트로 패킹하여 할당

        ```python
        numbers = [1, 2, 3, 4, 5]
        a, *b, c = numbers

        print(a)    # 1
        print(b)    # [2, 3, 4]
        print(c)    # 5
        ```


    - print 함수에서 임의의 가변 인자를 작성할 수 있었던 이유
    
        - 인자 개수 상관 없이 튜플 하나로 패킹 되어서 내부에서 처리

            ```python
            def my_func(*objects):
                print(objects)  # (1, 2, 3, 4, 5)
                print(type(objects))    # <class 'tuple'>

            my_func(1, 2, 3, 4, 5)
            # (1, 2, 3, 4, 5)
            # <class 'tuple'>
            ```

            ![alt text](./images/image_09.png)



### Unpacking

- Unpacking(언패킹)

    - 패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것



- 언패킹 예시

    - 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당

        ```python
        packed_values = 1, 2, 3, 4, 5
        a, b, c, d, e = packes_values

        print(a, b, c, d, e)    # 1 2 3 4 5
        ```


- '*'을 활용한 언패킹

    - *는 리스트의 요소를 언패킹하여 인자로 전달

        ```python
        def my_function(x, y, z):
            print(x, y, z)

        
        names = ['alice', 'jane', 'peter']
        my_function(*names) # alice jane peter
        ```



- '**'을 활용한 언패킹

    - **는 딕셔너리의 키-값 쌍을 언패킹하여 함수의 키워드 인자로 전달

        ```python
        def my_function(x, y, z):
            print(x, y, z)


        my_dict = {'x': 1, 'y': 2, 'z': 3}
        my_function(**my_dict)  # 1 2 3
        ```



- *, ** 패킹/ 언패킹 연산자 정리

    - '*'

        - 패킹 연산자로 사용될 때, 여러 개의 인자를 하나의 튜플로 묶음

        - 언패킹 연산자로 사용될 때, 시퀀스나 반복 가능한 객체를 각각의 요소로 언패킹하여 함수의 인자로 전달


    - '**'

        - 언패킹 연산자로 사용될 때, 딕셔너리의 키-값 쌍을 언패킹하여 함수의 키워드 인자로 전달



## 참고

- Lambda expression(람다 표현식)

    - 익명 함수를 만드는 데 사용되는 표현식(한 줄로 간단한 함수를 정의)


- lambda 표현식 구조

    ```python
    lambda 매개변수: 표현식
    ```

    - lambda 키워드

        - 람다 함수를 선언하기 위해 사용되는 키워드


    - 매개변수

        - 함수에 전달되는 매개변수들

        - 여러 개의 매개변수가 있을 경우 쉼표로 구분



    - 표현식

        - 함수의 실행되는 코드 블록으로, 결과값을 반환하는 표현식으로 작성



- lambda 표현식 예시

    - 간단한 연산이나 함수를 한 줄로 표현할 때 사용

    - 함수를 매개변수로 전달하는 경우에도 유용하게 활용

        ```python
        def addition(x, y):
            return x + y

        
        result = addtion(3, 5)
        print(result)   # 8
        ```

        ```python
        addition = lambda x, y: x + y

        result = addition(3, 5)
        print(result)   # 8
        ```


- 람다 표현식 활용(with map 함수)

    ```python
    numbers = [1, 2, 3, 4, 5]

    def square(x):
        return x**2


    # lambda 미사용
    squared1 = list(map(squre, numbers))
    print(squared1) # [1, 4, 9, 16, 25]

    # lambda 사용
    squared2 = list(map(lambda x: x**2, numbers))
    print(squared2) # [1, 4, 9, 16, 25]
    ```


---

## 함수
- Docstring : 설명서(선택)
- return 이후의 문장은 의미가 없어진다.
- print함수는 return(반환)이 있지만 그 return값이 None이다. => 출력하면 None이 출력된다.
- 함수의 호출은 함수의 실행이다.

## 매개변수와 인자
- 매개변수 : 
- 인자 : 
### 다양한 인자의 종류
- 위치 인자 : 위치인자는 함수 호출 시 반드시 값을 전달해야 함(누락되면 안된다.)
- 기본 인자 값 : 
- 키워드 인자 : 
- 임의의 인자 목록 : 개수가 정해져있지 않다.(print함수도 같은 이유로 여러 가지를 출력 가능) *로 처리 가능(여러 개의 인자를 tuple로 처리)
- 임의의 키워드 인자 목록 : **, 여러 개의 인자를 dictionary로 묶어 처리

### 재귀 함수
- 함수 내부에서 자기 자신을 호출하는 함수
- 종료 조건을 명확하게 설정해야 한다.

## 내장 함수(Built-in function)
- python이 기본적으로 제공하는 함수(별도의 import 없이 바로 사용 가능)
- 외장 함수라는 용어는 없다.
- ex. print, len, max, min, sum, sorted(슬라이싱을 통한 뒤집기[::-1]와 sorted는 다르다)

### 유용한 내장 함수 map & zip
#### map
- iterable : 반복 가능한 객체(요소), ex. 컬렉션
- map object결과를 list()로 변환해서 결과를 확인할 수 있다.
- 내가 만든 함수도 포함 가능하여 확장성이 넓고 다양하게 쓰인다.

#### zip
- zip(*iterables) : 임의의 iterable을 모아 tuple을 원소로 하는 zip object를 반환
- zip object결과를 list()로 변환해서 결과를 확인할 수 있다.
- 

## 함수와 scope
- 함수는 코드 내부에 

### global 키워드
- 변수의 scope를 전역 범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용
- global 키워드 선언 전에 참조 불가
- 매개변수에는 global 키워드 사용 불가

## Packing & Unpacking
### Packing
- 여러 개의 값을 **!!하나!!**의 변수에 묶어서 담는 것
- 하나의 변수에 할당할 때 tuple로
- *로 요소들을 패키할 때는 list로

### Unpacking
- 패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것
- *는 매개변수가 아닌 인자로 들어갈 때 쓰이면 리스트의 요소를 언패킹하여 인자로 전달한다.
- **는 딕셔너리의 키-값 쌍을 언패킹하여 함수의 키워드 인자로 전달(이때 매개변수의 이름과 인자로 들어가는 딕셔너리의 키 이름이 같아야 한다.)

## 참고
### Lambda expressions(람다 표현식)
- 익명 함수를 만드는 데 사용되는 표현식(한 줄로 간단한 함수를 정의)d
- 구성 : lambda 매개변수 : 표현식
    - lambda 키워드 : 
    - 매개변수 : 
    - 표현식 : 
- 명시도는 떨어질 수 밖에 없지만, 간단한 연산이나 함수를 한 줄로 표현할 수 있다.
- map과 유용하게 사용된다.
- 1회성으로 쓸 때 사용된다.