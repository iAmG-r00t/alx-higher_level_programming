-- list all genres not linked to the show Dexter
SELECT tv_genres.name AS name
FROM tv_genres
LEFT JOIN
(
	SELECT tv_genres.id, name
  FROM tv_genres
	JOIN tv_show_genres
	     ON tv_genres.id = tv_show_genres.genre_id
	JOIN tv_shows
	     ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = "Dexter"
	ORDER BY tv_genres.id
) dexter_genres ON dexter_genres.id = tv_genres.id
WHERE dexter_genres.id is NULL
ORDER BY name;
