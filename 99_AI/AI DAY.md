## AI DAY 시험 대비 내용 정리

#### 개발자에게 AI가 중요한 이유

- AI는 개발자의 업무 환경에도 많은 변화를 가져왔고 AI를 이해하고 활용할 줄 아는 개발자는 미래에 더욱 높은 경쟁력을 가질 수 있다.

  - 코드 생산성 UP

  - AI 소통 능력 UP

  - AI 문제 해결 역량 UP

  - 커리어 경쟁력 UP


#### AI 2번째 관점

- Programming

  - Data와 Program으로 Output을 만든다

- Machine Learning (Software 2.0)

  - Data와 Output으로 Program을 만든다.


#### Machine Learning & Deep Learning

- Traditional Machine Learning

  - input → Feature extraction → Classification → Output

- Deep Learning

  - input → End2End(Universal approximator)(Feature extraction + Classification) → Output


#### What is AI?

- Artificial Intelligence ⊃ Machine Learning ⊃ Deep Learning


#### It starts from a single neuron

- 1950년대에 이미 시작

- Perceptron : First real implementation of neural networks(뉴럴 네트워크의 첫 번째 시행)


#### Neural Networks

  ![alt text](./images/image_00.png)

  ![alt text](./images/image_01.png)


#### Single layer neural network (perceptron)

- 퍼셉트론의 활성화 함수

  - 신호가 역치 이상이면 값을 다른 뉴런에 전달하는 것을 모사하기 위해 활성화 함수로 계단 함수(Step function)을 활용

    ![alt text](./images/image_02.png)

    ![alt text](./images/image_03.png)


#### Return of the neural networks (in 2012)

- 합성곱 신경망 (CNN : Convolution Neural Networks)

  ![alt text](./images/image_04.png)

  ![alt text](./images/image_05.png)


- Pooling Layer

  - 큰 이미지를 처리하는 부담을 줄이기 위해 **중요한 정보로 요약**하고 불필요한 세부 사항은 생략

    ![alt text](./images/image_06.png)


#### 3 + Reasons of AI Success

- Computing HW + Data + Algorithm


#### Performance of NN is not saturated yet

- 뉴럴 네트워크의 performance는 아직 포화되지 않았다.

  ![alt text](./images/image_07.png)


#### How to Build AI

- Key Components of Deep Learning

  - Data : 모델이 학습할 데이터

  - Model : 입력 데이터를 우리가 원하는 출력으로 변환해주는 함수

  - Loss function : 모델의 출력을 통해 모델이 잘하는지 못하는지 판단해 수치화해주는 함수(매핑)

  - Algorithm : Loss를 줄여주기 위해 모델(파라미터)을 업데이트 하는 방법


#### AI의 디자인 요소 4(3)가지

- Big data

  - Data depend on the type of the problem to solve(Classification, Detection, Segmentation, etc.)

- Model

  - 영상인식 예시

    - Classifier : 입력 영상을 카테고리(클래스)로 매핑해주는 함수 f(.)

      ![alt text](./images/image_08.png)

  - Single layer neural network (perceptron)

    - 퍼셉트론

      - 각 입력값 $x_i$에 대한 가중치(weight) $w_i$가 존재할 때, 두 값을 곱한 $w_ix_i$ 벡터의 합으로 구성된 모델

      - 즉, **선형 결합** 관계에 있는 가중치로 구성된 모델 ($w^Tx + b$)

      - 활성화 함수 $\phi$를 통해 특정 임계값을 초과하는지를 기준으로 0 혹은 1의 값으로 결과 $y$를 출력

      - $y = \phi(w^T + b)$ ⇒ $y = \phi(x_0w_0 + x_1w_1 + x_2w_2 + \cdots + x_nw_n + b)$

        ![alt text](./images/image_09.png)
      

- Loss(Reward)

- Algorithm