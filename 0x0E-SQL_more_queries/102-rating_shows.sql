-- Task: 19. Rotten tomatoes

-- Use the hbtn_0d_tvshows_rate database
USE hbtn_0d_tvshows_rate;

-- Select show titles and their rating sums
SELECT tv_shows.title, SUM(tv_shows_rate.rating) AS rating_sum
FROM tv_shows
JOIN tv_shows_rate ON tv_shows.id = tv_shows_rate.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
