-- Active: 1728733986723@@127.0.0.1@3306

INSERT INTO
  employees (name, salary, age, departmentId)
VALUES
  ('이규보', 1700, 77, 1),
  ('김구', 126000, 35, 2),
  ('김철수', 23000, 35, 3),
  ('유관순', 82000, 45, 4);

UPDATE
  employees
SET
  age = 21
WHERE
  id = 10;


UPDATE
  employees
SET
  age = 37
WHERE
  id = 11;

UPDATE
  employees
SET
  age = 41
WHERE
  id = 12;



SELECT
  *
FROM
  employees;


-- 각 부서의 최고 연령 직원과 해당 부서의 평균 연령을 함께 조회
-- 부서별 최고나이, 평균나이, 가장 나이가 많은 직원의 이름 출력
SELECT
  departments.name AS 'department',
  employees.name AS 'oldest_employees',
  MAX(employees.age) AS 'max_age',
  AVG(employees.age) AS 'avg_age'
FROM
  employees
JOIN
  departments
ON employees.departmentId = departments.id
GROUP BY
  employees.departmentId;


-- 부서별로 가장 많은 급여를 받는 직원의 정보와 그 급여를 함께 조회
-- 부서별 가장 높은 연봉을 받는 직원의 연봉, 이름 출력
SELECT
  departments.name AS 'department',
  employees.name AS 'highest_paid_employee',
  MAX(salary) AS 'max_salary'
FROM
  employees
INNER JOIN
  departments
ON
  departments.id = employees.departmentId
GROUP BY
  employees.departmentId;


-- 부서별 연령대 별 직원 수 조회
-- 30세 이하, 30-40세 사이, 40세 이상
-- 각 부서별, 연령대별 직원 수 출력
SELECT
  departments.name AS 'department',
  CASE WHEN employees.age < 30 THEN 'Under 30'
       WHEN employees.age BETWEEN 30 AND 40 THEN 'BETWEEN 30~40'
       WHEN employees.age > 40 THEN 'Over 40'
  END AS 'age_group',
  COUNT(*) AS 'num_employees'
FROM
  employees
INNER JOIN
  departments
ON
  departments.id = employees.departmentId
GROUP BY
  departments.name,
  age_group;


-- 부서별로 최고 급여를 받는 직원을 제외한 평균 급여를 조회한다.
SELECT
  departments.name AS 'department',
  AVG(employees.salary) AS 'avg_salary_excluding_highest'
FROM
  employees
JOIN
  departments
ON
  employees.departmentId = departments.id
WHERE (employees.salary, employees.departmentId) NOT IN (
  SELECT
    MAX(salary),
    departmentId
  FROM
    employees
  GROUP BY
    departmentId
)
GROUP BY
  departments.id;


