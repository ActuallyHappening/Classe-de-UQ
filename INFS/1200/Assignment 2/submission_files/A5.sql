SELECT Username FROM User WHERE
	-- the number of posts for User.Username
    (SELECT COUNT(*) FROM Post WHERE Post.Username = User.Username)
    =
    -- The maximum number of posts
	(SELECT MAX(d.num_posts) as max_posts FROM (SELECT COUNT(*) as num_posts FROM Post GROUP BY Username) as d)