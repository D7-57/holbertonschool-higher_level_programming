-- 

SELECT tv_genres.name AS genre, count(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
     JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
