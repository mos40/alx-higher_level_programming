-- Task: 11. Genre ID for all shows

-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Select shows and genre IDs using a LEFT JOIN
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
