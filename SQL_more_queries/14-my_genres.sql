-- Importe el volcado de la base de datos de hbtn_0d_tvshows a su servidor MySQL (igual que 13-count_shows_by_genre.sql).
-- Utilza todos los datos de la database hbtn_0d_tvshows para enumerar los generos del programa 'Dexter'.

SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
