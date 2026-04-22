-- 12. Titles of all of movies in which both Jennifer Lawrence and Bradley Cooper starred

SELECT title FROM   movies
-- Create two lists
JOIN stars s1 ON movies.id = s1.movie_id
JOIN stars s2 ON movies.id = s2.movie_id
JOIN people p1 ON s1.person_id = p1.id
JOIN people p2 ON s2.person_id = p2.id
-- The condition is to look for an overlap from each list
WHERE  p1.NAME = "Bradley Cooper" AND p2.NAME = "Jennifer Lawrence";
