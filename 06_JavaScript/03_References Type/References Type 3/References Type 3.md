# 2024년 10월 25일(금) 수업 내용 정리 - References Type 3


- 배열

  - 배열 메서드


- Array helper method

  - 콜백 함수
  - forEach
  - map
  - 배열 순회 종합
  - 배열 with '전개 구문'


- 참고

  - 콜백 함수의 이점
  - forEach에서 break 사용하기
  - 배열은 객체다


## 배열

- Object

  - 키로 구분된 데이터 집합(data collection)을 저장하는 자료형

  - 이제는 **순서가 있는 collection**이 필요

- Array

  - 순서가 있는 데이터 집합을 저장하는 자료구조


- 배열 구조

  - 대괄호('[]')를 이용해 작성

  - 요소의 자료형은 제약 없음

  - length 속성을 사용해 배열에 담긴 요소 개수 확인 가능

    ![alt text](./images/image_00.png)




### 배열 메서드

- 주요 메서드

  |메서드|역할|
  |:--:|:--:|
  |push / pop|배열 끝 요소를 추가 / 제거|
  |unshift / shift|배열 끝 요소를 추가 / 제거|
  <br>


- push()

  - 배열 끝에 요소를 추가

    ![alt text](./images/image_01.png)


- pop()

  - 배열 끝 요소를 제거하고, 제거한 요소를 반환

    ![alt text](./images/image_02.png)


- unshift()

  - 배열 앞에 요소를 추가

    ![alt text](./images/image_03.png)


- shift()

  - 배열 앞 요소를 제거하고, 제거한 요소를 반환

    ![alt text](./images/image_04.png)




## Array helper method

- Array Helper Methods

  - 배열 조작을 보다 쉽게 수행할 수 있는 특별한 메서드 모음


- Array Helper Methods

      - ES6에 도입

      - 배열의 각 요소를 순회하며 각 요소에 대해 함수(콜백함수)를 호출

      - 대표 메서드

        - forEach(), map(), filter(), every(), some(), reduce() 등

      - 메서드 호출 시 인자로 함수(콜백함수)를 받는 것이 특징




### 콜백 함수

- 콜백 함수(Callback function)

  - 다른 함수에 인자로 전달되는 함수

  - 외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행


- 콜백 함수 예시

  ![alt text](./images/image_05.png)


- 주요 Array Helper Methods

  |메서드|역할|
  |:--:|:--|
  |forEach|- 배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출<br>- 반환 값 없음|
  |map|- 배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출<br>- 함수 호출 결과를 모아 새로운 배열을 반환|
  <br>



### forEach

- forEach()

  - 배열의 각 요소를 반복하며 모든 요소에 대해 함수(콜백함수)를 호출


- forEach 구조

  ![alt text](./images/image_06.png)

  ![alt text](./images/image_07.png)

  - 콜백함수는 3가지 매개변수로 구성

    1. item : 처리할 배열의 요소

    2. index : 처리할 배열 요소의 인덱스 (선택 인자)

    3. array : forEach를 호출한 배열 (선택 인자)

  - 반환 값

    - undefined

  
- forEach 예시

  ![alt text](./images/image_08.png)

  - 출력 결과

  ![alt text](./images/image_09.png)


- forEach 활용

  - forEach의 인자를 모두 활용

    ![alt text](./images/image_10.png)

    - 출력 결과

    ![alt text](./images/image_11.png)




### map

- map()

  - 배열의 모든 요소에 대해 함수(콜백함수)를 호출하고, 반환된 호출 결과 값을 모아 **새로운 배열을 반환**


- map 구조

  ![alt text](./images/image_12.png)

  ![alt text](./images/image_13.png)

  - forEach의 매개 변수와 동일

  - 반환 값

    - 배열의 각 요소에 대해 실행한 "callback의 결과를 모은 새로운 배열"

    - forEach 동작 원리와 같지만 forEach와 달리 **새로운 배열을 반환**함


- map 예시

  - 배열을 순회하며 각 객체의 name 속성 값을 추출하기 (for...of 와 비교)

    ![alt text](./images/image_14.png)


- map 활용

  ![alt text](./images/image_15.png)

  ![alt text](./images/image_16.png)


- python에서의 map 함수와 비교

  - python의 map에 square 함수를 인자로 넘겨 numbers 배열의 각 요소를 square 함수의 인자로 사용하였음

    ![alt text](./images/image_17.png)

  - map 메서드에 callBackFunc 함수를 인자로 넘겨 numbers 배열의 각 요소를 callBackFunc 함수의 인자로 사용하였음

    ![alt text](./images/image_18.png)




### 배열 순회 종합

### 배열 with '전개 구문'


## 참고

### 콜백 함수의 이점

### forEach에서 break 사용하기

### 배열은 객체다