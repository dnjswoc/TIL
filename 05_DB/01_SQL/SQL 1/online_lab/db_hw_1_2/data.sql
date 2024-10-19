-- Active: 1728528109958@@127.0.0.1@3306
-- 1. tracks 테이블의 모든 데이터를 조회하시오.
SELECT
  *
FROM
  tracks;


-- 2. Name, Milliseconds, UnitPrice 열의 모든 데이터를 조회하시오.
SELECT
  Name, Milliseconds, UnitPrice
FROM
  tracks;


-- 3. GenreId 행의 값이 1인 모든 데이터를 조회하시오.
SELECT
  *
FROM
  tracks
WHERE
  GenreId = 1;


-- 4. 모든 데이터를 name을 기준으로 오름차순 정렬하여 조회하시오.
SELECT
  *
FROM
  tracks
ORDER BY
  Name ASC;


-- 5. tracks 테이블의 모든 데이터를 조회하되, 10개만 출력하시오.
SELECT
  *
FROM
  tracks
LIMIT
  10;