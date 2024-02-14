-- Script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT title, SUM(tv_show_rating.rate) 'rating'
FROM tv_shows
LEFT JOIN tv_show_rating ON tv_shows.id = tv_show_rating.show_id
GROUP BY title
ORDER BY rating DESC;
