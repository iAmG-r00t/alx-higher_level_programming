-- lists all shows contained in the database
-- CREATE A NEW DB
-- CREATE DATABASE hbtn_0d_tvshows
-- impoer sql data
-- USE hbtn_0d_tvshows.sql
-- source hbtn_0d_tvshows.sql
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id ASC;
