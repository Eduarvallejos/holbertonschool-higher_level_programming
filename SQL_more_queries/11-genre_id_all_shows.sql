-- Importe el volcado de la base de datos de hbtn_0d_tvshows a su servidor MySQL (igual que 10-genre_id_by_show.sql).
-- Este script enumera todos los programas contenidos en la database hbtn_0d_tvshows.
-- Si un programa no tiene un género, muestra NULL.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
