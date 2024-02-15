-- Task: 16. List shows and genres
-- Select titles and genres using a LEFT JOIN
SELECT tv_shows.title, tv_genres.name
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;
