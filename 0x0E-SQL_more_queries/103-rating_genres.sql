-- Script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT name, SUM(tv_show_ratings.rate) rating
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_show_genres.show_id
GROUP BY name
ORDER BY rating DESC;
