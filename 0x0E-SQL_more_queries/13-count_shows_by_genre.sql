-- Task: 13. Number of shows by genre
-- Use the hbtn_0d_tvshows database
-- Select genres and count of shows using a JOIN and GROUP BY
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
