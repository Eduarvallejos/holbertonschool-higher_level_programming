-- Importe el volcado de la base de datos de hbtn_0d_tvshows a su servidor MySQL (igual que 14-my_genres.sql).
-- Este script enumera todos los programas de comedia de la database hbtn_0d_tvshows.

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
