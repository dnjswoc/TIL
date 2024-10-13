-- Active: 1728728972767@@127.0.0.1@3306
-- 2. BillingState에 저장되어 있는 데이터 값은 주 이름의 약자로 저장
-- a. BillingCountry를 기준으로 그룹화하고, 각 나라별 총판매액을 계산하여 조회하시오
SELECT
  BillingCountry,
  SUM(Total) AS 'TotalSales'
FROM
  invoices
GROUP BY
  BillingCountry;


-- b. InvoiceDate를 연도별로 그룹화하고, 각 연도별 총판매액을 계산하여 조회하시오
SELECT
  strftime('%Y', InvoiceDate) AS 'YEAR',
  SUM(Total) AS 'TotalSales'
FROM
  invoices
GROUP BY
  YEAR;


-- c. BillingCountry이 USA이고 InvoiceDate가 2010년 01년 01 이후인
-- 레코드를 BillingState를 기준으로 그룹화하고, 각 주별로 총 주문 금액을 계산하여 조회하시오
SELECT
  BillingState,
  SUM(Total) AS 'TotalSales'
FROM
  invoices
WHERE
  BillingCountry = 'USA'
  AND InvoiceDate >= '2010-01-01'
GROUP BY
  BillingState


-- d. BililngCountry이 Germany이거나 BillingCountry이 France인
-- 레코드를 BillingCountry를 기준으로 그룹화하고, 각 나라별로 최대 주문 금액을 계산하여 조회하시오
SELECT
  BillingCountry,
  MAX(Total) AS 'MaxOrderAmount'
FROM
  invoices
WHERE
  BillingCountry IN ('Germany', 'France')
GROUP BY
  BillingCountry;