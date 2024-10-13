-- Active: 1728568440755@@127.0.0.1@3306
-- 1. age가 30세 이상이면서 balance가 1000 이상인 사용자들의 정보를 조회하시오
SELECT
  *
FROM
  users
WHERE
  age >= 30
  AND balance >= 1000;


-- 2. balance가 1000 이하인 사용자들 중에서 age가 20세 이하인
-- 사용자들의 정보를 조회하시오.
SELECT
  *
FROM
  users
WHERE
  balance <= 1000
  AND age <= 20;


-- 3. first_name이 '현'으로 시작하고 country가 '제주특별자치도'인
-- 사용자들 중에서 가장 age가 많은 사용자의 정보를 조회하시오.
SELECT
  *
FROM
  users
WHERE
  first_name LIKE '현%'
  AND country = '제주특별자치도'
ORDER BY
  age DESC
LIMIT 1;



-- 4. last_name이 '박'이고 age가 25세 이상인 사용자들 중에서 가장 age가 어린
-- 사용자의 정보를 조회하시오.
SELECT
  *
FROM
  users
WHERE
  last_name = '박'
  AND age >= 25
ORDER BY
  age
LIMIT 1;


-- 5. first_name이 '재은'이거나 '영일'인 사용자들 중에서 balance가 가장 많은
-- 사용자의 정보를 조회하시오
SELECT
  *
FROM
  users
WHERE
  first_name IN ('재은', '영일')
ORDER BY
  balance
LIMIT 1;


-- 6. 각 country 별로 가장 많은 balance를 가진 사용자의 정보를 조회하고
-- balance를 내림차순 정렬하시오.
SELECT
  first_name, last_name, age, phone, country, MAX(balance) AS 'max_balance'
FROM
  users
GROUP BY
  country
ORDER BY
  max_balance DESC;

-- SELECT
--   *
-- FROM
--   users
-- GROUP BY
--   country
-- HAVING
--   MAX(balance)
-- ORDER BY
--   balance DESC;


-- 7. age가 30세 이상이면서, balance가 age가 30세 이상인 사용자들의 평균 balance보다
-- 높은 사용자의 정보를 조회하시오
SELECT
  *
FROM
  users
WHERE
  age >= 30
  AND balance > (
    SELECT
      AVG(balance)
    FROM
      users
    WHERE
      age >= 30
  );