-- Active: 1728530674991@@127.0.0.1@3306
-- 1. age가 18세 미만인 유저를 age 기준으로 내림차순으로 정렬하여 조회하시오.
SELECT
  *
FROM
  users
WHERE
  age < 18
ORDER BY
  age DESC;


-- 2. age가 18세 미만인 유저의 last_name과 age 필드만 출력하되, last_name 기준으로 우선 오름차순 정렬하고,
-- last_name이 같은 경우, age 기준으로 다시 내림차순 정렬하여 조회하시오.
SELECT
  last_name, age
FROM
  users
WHERE
  age < 18
ORDER BY
  last_name ASC,
  age DESC;


-- 3. 2번과 동일한 조회를 하되, last_name과 age가 동일한 중복 데이터를 제외하고 조회하시오.
SELECT DISTINCT
  last_name, age
FROM
  users
WHERE
  age < 18
ORDER BY
  last_name ASC,
  age DESC;