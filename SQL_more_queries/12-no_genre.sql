-- Importe el volcado de la base de datos de hbtn_0d_tvshows a su servidor MySQL (igual que 11-genre_id_all_shows.sql).
-- Este script enumera todos los programas contenidos dentro de la database hbtn_0d_tvshows sin un genero vinculado.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
