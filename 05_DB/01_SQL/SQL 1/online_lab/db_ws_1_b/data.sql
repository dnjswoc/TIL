-- Active: 1728571102889@@127.0.0.1@3306
SELECT
  *
FROM
  songs;


SELECT
  *
FROM
  songs
ORDER BY
  title DESC;


SELECT
  *
FROM
  songs
WHERE
  genre = 'Pop';


SELECT
  *
FROM
  songs
WHERE
  duration >= 180;