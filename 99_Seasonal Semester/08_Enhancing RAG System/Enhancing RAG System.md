# 2024년 12월 26일(목) 수업 내용 정리 - Enhancing RAG System


## 벡터 데이터베이스 검색 정확도 향상 기법

- 데이터 최적화

- Vector DB 선택하기

- Retriever 최적화


### 1. 데이터 최적화

#### Data Chunking

- Chunking이란?

  ![alt text](./images/image_00.png)

  - Embedding의 단위가 되는 텍스트를 정하는 작업

  - Retrieve 대상의 단위

  - 단순히 길이를 기준으로 자르는 경우

    - 의미가 담기는 단위 : 단어 / 구 / 절 / 문장 / 문단

    - 단순히 길이를 기준으로 자르는 것은 좋지 않음

  - Semantic Chunking : 의미가 비슷한 문장들을 묶을 수 있음

    - Langchain의 구현체는 Hierarchical Clustering을 사용


- Recursive Text Splitter

  ![alt text](./images/image_01.png)

  - 가장 대표적으로 사용되는 Chunking 방법론 중 하나

  - 텍스트 분할 방식 : '\n\n' > '\n' > '' > '' 순서대로 token을 적용

    - 큰 단위부터 순서대로 텍스트들을 분할하여 주어진 chunk size를 넘지않게 함

  - 파라미터

    - chunk_size : 하나의 chunk 크기

    - chunk_overlap을 적용하여 어느정도 겹쳐서 나눔으로써 문장이 부자연스럽게 나뉠 가능성을 낮춤

  - 위 두 개의 값을 잘 조정해서 문맥을 잃지 않으면서 적당한 단위로 나누는 것이 목표


- Semantic Chunker

  ![alt text](./images/image_02.png)

  - 문장을 의미 단위로 분할하는 방법론

  - 텍스트 청킹 방식 : 임베팅 모델을 활용하여 문장을 임베딩 한 후, 백분위수, 표준편차 등의 분할 기준점에 따라 의미가 유사한 문장들을 병합

<hr>

#### Metadata

![alt text](./images/image_03.png)

- 검색 대상의 external information을 추가하여 filtering이나 reranking에 활용

- Ex. 논문-키워드, 저자, 소속기관, 출판연도 등
- Ex. 뉴스기사-키워드, 작성자, 발행일시, 발행기관 등

  - 직접적인 데이터 정보로 연관성이 있는 정보 체크

<hr>

#### Preprocessing

- 데이터 전처리

  - 원본 텍스트의 퀄리티가 Embedding 성능에 영향을 미침

  - 데이터 전처리 방법론

    - 데이터 노이즈 제거 : 의미없는 특수문자, 비문 등을 제거하는 것이 좋음

    - 텍스트 정제 : 오타, 띄어쓰기 수정

    - 표현 통합 : 같은 의미를 가지지만 다르게 표현된 표현들은 하나의 형태로 통합하면 성능 향상에 도움

    - 언어 통일 : multilingual corpus의 경우 번역기를 이용해서 하나의 언어로 통일하는 방법도 가능

<hr>

#### Embedding Model

- Embedding Model : 오픈소스로 공개되어 있는 pretrained model을 사용

- Embedding Model 선택 시 기준

  ① 해당 임베딩 모델이 어떤 텍스트를 학습했는 지
  
  ② (특히 지원하는 언어의) 성능을 확인하는 것이 중요함
  
  ③ 일반적으로 임베딩 공간의 크기가 클수록 성능이 뛰어나며 대신에 inference 속도가 느림
  
  ④ 대부분 최신에 나온 임베딩 모델일수록 성능이 높은 편

- 대표적인 임베딩 및 플랫폼

  - OpenAIEmbeddings : 가장 많이 활용됨

  - HuggingfaceEmbeddings : 공개된 embedding model을 사용할 수 있는 플랫폼

![alt text](./images/image_04.png)

- Upstage Solar Embeddings

  ![alt text](./images/image_05.png)

  - 긴 텍스트와 문맥 정보를 효과적으로 처리하며, 높은 검색 정확도를 제공

  - **우수한 다국어 성능** : OpenAI의 text-embedding-3-large를 능가하며 영어, 한국어, 일본어 등 다양한 언어에서 뛰어난 성능 발휘

  - **벤치마크 성과** : MTEB 및 MIRACL에서 우수한 성과를 기록, 특히 까다로운 작업에서도 높은 성능 보장

<hr>

### 2. Vector DB 선택하기

#### Vector Store

- Vector DB 선택 시 고려사항

  - 각 Vector Store(= Vector Index) 마다 지원하는 방식과 구현 상의 차이가 있음

  - 각 방식마다 개발된 목적이 다르기 때문에 서비스 상황에 맞는 것을 골라서 사용해야 함

  - 특히, 벡터 데이터베이스마다 지원하는 검색 알고리즘이 다름

  - 대표적인 벡터 데이터베이스 : FAISS, ChromaDB, Milvus, Pinecone, Qdrant, Redis


- 로컬 vs 클라우드 데이터베이스

  - 로컬(Local)

    - 장점 : 데이터에 대한 완전하 제어권을 유지할 수 있고, 네트워크 의존성이 낮음

    - 단점 : 데이터 양이 많을수록 레이턴시 증가함

    - 예시. Chroma, FAISS

  - 클라우드(Cloud)

    - 장점 : 확장성이 우수하고, 대용량 데이터에서도 빠른 성능을 제공함

    - 단점 : 네트워크 의존성이 있음

    - 예시. Pinecone, Weaviate


