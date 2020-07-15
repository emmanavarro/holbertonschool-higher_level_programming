-- Lists all Comedy shows in the database hbtn_0d_tvshows
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
SELECT ts.title FROM tv_shows ts INNER JOIN tv_show_genres tsg ON tsg.show_id = ts.id INNER JOIN tv_genres tg ON tg.id = tsg.genre_id WHERE tg.name = 'Comedy' GROUP BY ts.title ORDER BY ts.title ASC;
