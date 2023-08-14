-- scirpt that lists all genres and displays the number of shows linked to each
SELECT tv_genres.name AS genre, number_of_shows
COUNT(*) 
ORDER BY number_of_shows DESC;
