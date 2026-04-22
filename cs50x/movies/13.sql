-- 13. Names of all people who starred in a movie in which Kevin Bacon also starred

-- Work inside out
SELECT DISTINCT(name) FROM people
WHERE id IN (
    -- Get ids of everyone in those movies LAST HERE
    SELECT person_id FROM stars
    WHERE movie_id IN (
        -- Get movie_ids that Kevin Bacon starred in THEN HERE
        SELECT movie_id FROM stars
        WHERE person_id = (
            -- Get Kevin Bacon's ID START HERE
            SELECT id FROM people
            WHERE name = 'Kevin Bacon' AND birth = 1958
        )
    )
)
-- Exclude Kevin Bacon as per spec
AND name != 'Kevin Bacon';
