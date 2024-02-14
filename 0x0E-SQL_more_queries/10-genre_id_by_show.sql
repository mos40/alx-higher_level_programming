-- Task: 10. Genre ID by Show

-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Select shows and genre IDs using a JOIN
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
