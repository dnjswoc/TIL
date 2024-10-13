-- Active: 1728531586983@@127.0.0.1@3306
-- 1. 전체 사용자의 평균 age를 구하시오.
SELECT
  AVG(age) AS average_age
FROM
  users;


-- 2. 각 country 별로 사용자 수를 구하시오.
SELECT
  country, COUNT(*) AS 'user_count'
FROM
  users
GROUP BY
  country;


-- 3. balance가 가장 많은 사용자의 정보 중, 가장 먼저 조회되는 한 명의 정보만 조회하시오.
SELECT
  *
FROM
  users
ORDER BY
  balance DESC
LIMIT
  1;


-- 4. 각 country 별로 평균 balance를 구하시오.
SELECT
  country, AVG(balance) AS 'avg_balance'
FROM
  users
GROUP BY
  country;


-- 5. balance가 가장 많은 사용자와 가장 적은 사용자의 balance 차이를 구하시오.
SELECT
  (MAX(balance) - MIN(balance)) AS 'balance_difference'
FROM
  users;
