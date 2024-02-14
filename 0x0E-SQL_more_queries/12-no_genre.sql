-- Task: 12. No genre

-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Select shows without a genre using a LEFT JOIN and IS NULL condition
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
