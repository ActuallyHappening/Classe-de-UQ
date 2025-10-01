-- I'm not sure if this is taught in the INFS1200 syllabus
-- SELECT COUNT(*) as num_posts FROM (SELECT DISTINCT PostId FROM PostImage WHERE ImageURL LIKE "https://antisocial.media%") as d
-- Handles edge case where a post has multiple matching images uploaded
SELECT COUNT(DISTINCT PostId) as num_posts FROM PostImage WHERE ImageURL LIKE "https://antisocial.media%"
