-- Active: 1728531148622@@127.0.0.1@3306
-- 1. 사용자 중에서 first_name이 '하'로 시작하는 사용자의 정보를 조회하시오.
SELECT
  *
FROM
  users
WHERE
  first_name LIKE '하%';


-- 2. phone이 '555'로 끝나는 사용자들의 정보를 조회하시오.
SELECT
  *
FROM
  users
WHERE
  phone LIKE '%555';


-- 3. country가 '경상'으로 시작하는 사용자들의 정보를 조회하시오.
SELECT
  *
FROM
  users
WHERE
  country LIKE '경상%';



-- 4. country가 '경' 또는 '충'으로 시작하고, 세 번째 글자가 '남'인 사용자들의 정보를 조회하시오.
SELECT
  *
FROM
  users
WHERE
  (country LIKE '경%'
  OR country LIKE '충%')
  AND country LIKE '__남%';
