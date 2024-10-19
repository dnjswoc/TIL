-- Active: 1728731853599@@127.0.0.1@3306
SELECT
  *
FROM
  hotels;


-- grade 필드의 값을 모두 대문자로 수정
UPDATE
  hotels
SET
  grade = UPPER(grade);


-- customers 테이블 생성
CREATE TABLE customers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL
);


-- reservations 테이블 생성
CREATE TABLE reservations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER NOT NULL,
  room_num TEXT NOT NULL,
  check_in TEXT NOT NULL,
  check_out TEXT NOT NULL,
  FOREIGN KEY (customer_id)
    REFERENCES customers(id),
  FOREIGN KEY (room_num)
    REFERENCES hotels(room_num)
);

PRAGMA table_info('reservations');


-- 데이터 삽입
INSERT INTO
  customers (name, email)
VALUES
  ('홍길동', 'john@example.com'),
  ('박지영', 'jane@example.com'),
  ('김미영', 'alice@example.com'),
  ('이철수', 'bob@example.com');

INSERT INTO
  reservations (customer_id, room_num, check_in, check_out)
VALUES
  (1, '101', '2024-03-20', '2024-03-25'),
  (2, '202', '2024-03-21', '2024-03-24'),
  (3, '303', '2024-03-22', '2024-03-26'),
  (4, '404', '2024-03-23', '2024-03-27');


-- 데이터 조회
SELECT
  *
FROM
  customers;

SELECT
  *
FROM
  reservations;