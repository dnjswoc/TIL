-- Active: 1728570339883@@127.0.0.1@3306
CREATE TABLE songs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  artist TEXT NOT NULL,
  album TEXT NOT NULL,
  genre TEXT NOT NULL,
  duration INTEGER NOT NULL
);

INSERT INTO
  songs (title, artist, album, genre, duration)
VALUES
  ('Song 1', 'Artist 1', 'Album 1', 'Pop', 200),
  ('Song 2', 'Artist 2', 'Album 2', 'Rock', 300),
  ('Song 3', 'Artist 3', 'Album 3', 'Hip Hop', 250),
  ('Song 4', 'Artist 4', 'Album 4', 'Electronic', 180),
  ('Song 5', 'Artist 5', 'Album 5', 'R&B', 320);

SELECT
  *
FROM
  songs;

UPDATE
  songs
SET
  title = 'New Title'
WHERE
  id = 1;