-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
  -- Each record should display: tv_shows.title - tv_shows_genres.genre_id
  -- results should be in ascending order by tv_shows.title and tv_show_genres.genre_id
  -- you can use only SELECT statement
USE hbtn_0d_tvshows;
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.genre_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

