-- Active: 1728727606564@@127.0.0.1@3306
-- 1. InvoiceId와 InvoiceDate 열만 선택하여 조회하시오
SELECT
  InvoiceId, InvoiceDate
FROM
  invoices;



-- 2. BillingCountry 값이 USA이고 Total이 10보다 큰 레코드만
-- 선택하여 조회하시오
SELECT
  *
FROM
  invoices
WHERE
  BillingCountry = 'USA'
  AND Total > 10;


-- 3. BillingCity가 London이거나 Berlin인 레코드를 선택하여 조회하시오
SELECT
  *
FROM
  invoices
WHERE
  BillingCity IN ('London', 'Berlin');



-- 4. Total이 가장 큰 레코드를 선택하여 조회하시오
SELECT
  *
FROM
  invoices
ORDER BY
  Total DESC
LIMIT
  1;


-- 5. InvoicedDate가 2013년 3월 31일 이후이고 Total이 3보다
-- 큰 레코드만 선택하여 조회하시오
SELECT
  *
FROM
  invoices
WHERE
  InvoiceDate >= '2013-03-31'
  AND Total > 3;



-- 6. BillingCountry이 USA이고 BillingState가 California이며
-- Total이 10보다 큰 레코드를 선택하여 조회하시오
SELECT
  *
FROM
  invoices
WHERE
  BillingCountry = 'USA'
  AND BillingState = 'CA'
  AND Total > 10;


-- 7. BillingCountry이 Canada이고 BillingState이 Ontario이며
-- BillingCity이 Toronto인 레코드를 선택하여 조회
SELECT
  *
FROM
  invoices
WHERE
  BillingCountry = 'Canada'
  AND BillingState = 'ON'
  AND BillingCity = 'Toronto';



-- 8. InvoiceDate가 2023년 1월 1일 이전이고
-- (Total이 40보다 이상이거나 BillingCountry가 Brazil인)
-- 레코드를 선택하여 조회하시오
SELECT
  *
FROM
  invoices
WHERE
  InvoiceDate < '2023-01-01'
  AND (
    Total >= 40
    OR BillingCountry = 'Brazil'
  );