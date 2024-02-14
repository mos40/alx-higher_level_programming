-- Task: 20. Best genre

-- Use the hbtn_0d_tvshows_rate database
USE hbtn_0d_tvshows_rate;

-- Select genre names and their rating sums
SELECT tv_genres.name, SUM(tv_shows_rate.rating) AS rating_sum
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows_rate ON tv_show_genres.show_id = tv_shows_rate.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
