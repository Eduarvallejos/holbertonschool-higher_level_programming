-- Se importa el volcado de la database de hbtn_0d_tvshows a mi servidor MYSQL.
-- Enumera todos los programas contenidos en hbtn_0d_tvshows
-- Que tengan al menos un genero vinculado.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
