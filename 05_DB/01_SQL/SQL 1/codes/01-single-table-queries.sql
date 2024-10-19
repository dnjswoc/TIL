-- Active: 1728521367786@@127.0.0.1@3306
-- 01. Querying data
SELECT 
  LastName
FROM
  employees;

SELECT 
  LastName, FirstName
FROM
  employees;

SELECT 
  *
FROM
  employees;

# 별칭설정 AS 글자 제외해도 되는데, 이래도 되냐?
# -> 된다. 단, 명시성이 많이 떨어진다.
# AS 설정할때, '이름' 이라고 '' 안붙여도 되던데 그래도 되나요? 
# -> 명시성 때문이기도 한데... 가장 간단한 이유는... `이름 이에요` 이라고 한다면?
  # 공백을 기준으로 키워드를 구분하기 때문에... `이에용`이뭔지 모른다. 문법 에러 발생
  # 그럴떄 ''로 감싸준다 -> 문자열 이라는 의미였다. (문자열에서 공백은? 중요한 값중 하나다.)
  # '안녕하세요' 와 '안녕 하세요'는 완전히 다른 문자열
SELECT 
  e.FirstName AS '이름 이에용', 
  e.LastName '성', 
  a.AlbumId '앨범 아이디'
FROM 
  employees AS e
JOIN albums AS a  
;

SELECT 
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM 
  tracks;


-- 02. Sorting data
SELECT 
  FirstName
FROM
  employees
ORDER BY
  FirstName;

SELECT 
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;

# 오름차순정렬을 위한 ASC는 생략 가능하다.
# 근데 표기해 주는게 명시적으로는 맞기는한데...
SELECT 
  Country, City
FROM
  customers
ORDER BY
  Country DESC,
  City ASC;

SELECT 
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM 
  tracks
ORDER BY
  Milliseconds DESC;


-- NULL 정렬 예시
SELECT 
  postalCode
FROM
  customers
ORDER BY
  postalCode;


-- 03. Filtering data
SELECT
  Country
FROM
  customers
ORDER BY
  Country;

SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;

SELECT 
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';

SELECT 
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'Prague';

SELECT 
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  AND Country = 'USA';

SELECT 
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  OR Country = 'USA';

SELECT 
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000;
-- WHERE
--   Bytes >= 10000
--   AND Bytes <= 50000;

SELECT 
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000
ORDER BY Bytes;

SELECT 
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country IN ('Canada', 'Germany', 'France');
-- WHERE
--   Country = 'Canada'
--   OR Country = 'Germany'
--   OR Country = 'France';

SELECT 
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country NOT IN ('Canada', 'Germany', 'France');

SELECT 
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son';

SELECT 
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a';

# 아래처럼 적어도 되느냐? -> 된다.
# 되는데... 문제는 LENGTH 함수가 SQL 표준으로 보기 어렵다.
SELECT 
  LastName, FirstName
FROM
  customers
WHERE
  LENGTH("FirstName") = 4
  AND
  FirstName LIKE '___a';

CREATE TABLE test (
  title TEXT
);

INSERT INTO test VALUES ('한글');
INSERT INTO test VALUES ('ENGLISH');

SELECT LENGTH(title) FROM test;



SELECT 
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY Bytes DESC
LIMIT 7;


SELECT 
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY 
  Bytes DESC
LIMIT 3, 4;
-- LIMIT 4 OFFSET 3;



-- 04. Grouping data
SELECT 
  c1, c2,..., cn, aggregate_function(ci)
FROM
  table_name
GROUP BY 
  c1, c2, ..., cn;

SELECT
  Country
FROM
  customers
GROUP BY
  Country;

SELECT 
  Country, COUNT(*)
FROM
  customers
GROUP BY 
  Country;

SELECT
  Composer,
  AVG(Bytes)
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  AVG(Bytes) DESC;

SELECT
  Composer,
  AVG(Bytes) AS avgOfBytes
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  avgOfBytes DESC;

-- 에러
SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
WHERE 
  avgOfMinute < 10
GROUP BY
  Composer;

-- 에러 해결
SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
GROUP BY
  Composer
HAVING
  avgOfMinute < 10;
