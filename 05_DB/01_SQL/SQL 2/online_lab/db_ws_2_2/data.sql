-- Active: 1728730791135@@127.0.0.1@3306
-- 1. zoo 테이블에 species 열을 추가한다. 값은 Text를 받을 수 있어야 한다.
ALTER TABLE
  zoo
ADD COLUMN
  species TEXT NOT NULL DEFAULT 'default value';



-- 2. zoo 테이블에 삽입되어 있는 모든 데이터에 species 값을 추가하여 수정
UPDATE
  zoo
SET
  species = 'Panthera leo'
WHERE
  name = 'Lion';

UPDATE
  zoo
SET
  species = 'Loxodonta africana'
WHERE
  name = 'Elephant';

UPDATE
  zoo
SET
  species = 'Giraffe camelopardalis'
WHERE
  name = 'Giraffe';

UPDATE
  zoo
SET
  species = 'Cebus capucinus'
WHERE
  name = 'Monkey';



-- 3. 모든 데이터의 height 값을 2.54가 곱해진 값으로 수정
UPDATE
  zoo
SET
  height = height * 2.54;


-- 4. zoo 테이블의 모든 데이터를 조회하여 출력
SELECT
  *
FROM
  zoo;