-- Task: 16. List shows and genres

-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Select titles and genres using a LEFT JOIN
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
