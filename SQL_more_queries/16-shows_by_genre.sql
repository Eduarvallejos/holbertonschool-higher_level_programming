-- Import the database dump from hbtn_0d_tvshows to your MySQL server (same as 15-comedy_only.sql).
-- Este script enumera todos los programas y los generos vinculados a cada uno.
-- Si un programa no tiene genero mostrara NULL.

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
