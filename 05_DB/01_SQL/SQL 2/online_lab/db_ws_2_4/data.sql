-- Active: 1728732713598@@127.0.0.1@3306
-- transactions 테이블 생성
CREATE TABLE transactions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  amount TEXT NOT NULL,
  transaction_date DATE NOT NULL,
  FOREIGN KEY (user_id)
    REFERENCES users(id)
);

PRAGMA table_info('transactions');

-- 데이터 삽입
INSERT INTO
  transactions (user_id, amount, transaction_date)
VALUES
  (1, '500', '2024-03-15'),
  (2, '700', '2024-03-16'),
  (1, '200', '2024-03-17'),
  (3, '1000', '2024-03-18');

SELECT
  *
FROM
  transactions;


-- users 테이블의 각 user 별 first_name, last_name, amount, transaction_date 조회
SELECT
  users.first_name, users.last_name, transactions.amount, transactions.transaction_date
FROM
  users
INNER JOIN
  transactions
ON
  transactions.user_id = users.id;


-- users 테이블의 각 user 별 거래일자가 '2024-03-16'이후인 데이터의
-- first_name, last_name, amount, transaction_date 조회
SELECT
  users.first_name, users.last_name, transactions.amount, transactions.transaction_date
FROM
  users
INNER JOIN
  transactions
ON
  transactions.user_id = users.id
WHERE
  transaction_date > '2024-03-16';


-- users 테이블의 각 user 별 first_name, last_name, 총 거래량(total_amount) 조회
-- user id를 기준으로 그룹화하여 해당 user의 amount 총 량 출력
SELECT
  users.first_name, users.last_name, SUM(transactions.amount) AS 'total_amount'
FROM
  users
INNER JOIN
  transactions
ON
  transactions.user_id = users.id
GROUP BY
  users.id;