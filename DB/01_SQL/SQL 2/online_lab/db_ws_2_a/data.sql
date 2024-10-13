-- Active: 1728725269452@@127.0.0.1@3306

-- 1. artists 테이블에서 모든 아티스트의 정보를 조회하시오.
SELECT
  *
FROM
  artists;


-- 2. artists 테이블의 모든 데이터의 수를 조회하시오
SELECT
  COUNT(*)
FROM
  artists;


-- 3. artists 테이블에서 Name이 'AC/DC'인 정보를 조회하시오.
SELECT
  *
FROM
  artists
WHERE
  Name = 'AC/DC';


-- 4. artists 테이블의 모든 데이터 중, artistid와 Name만 출력하시오.
SELECT
  ArtistId, Name
FROM
  artists;



-- 5. artists 테이블에서 Name이 'Gilberto Gil'이거나
-- 'Ed Motta' 정보를 조회하시오
SELECT
  *
FROM
  artists
WHERE
  Name IN ('Gilberto Gil', 'Ed Motta');


-- 6. artists 테이블에서 모든 정보를 Name 기준으로 내림차순 정렬하여 조회하시오
SELECT
  *
FROM
  artists
ORDER BY
  Name DESC;


-- 7. artists 테이블에서 이름이 VinIcius로 시작하는 정보를 조회하시오.
-- 단, 2개까지만 출력되도록 한다
SELECT
  *
FROM
  artists
WHERE
  Name LIKE 'Vinícius%'
LIMIT
  2;


-- 8. artists 테이블에서 ArtistId가 50번부터 70번까지의
-- 데이터를 조회하여 ArtistId만 출력하시오
SELECT
  ArtistId
FROM
  artists
WHERE
  ArtistId BETWEEN 50 AND 70;