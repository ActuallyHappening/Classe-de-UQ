CREATE OR REPLACE VIEW NumFollowers AS
	SELECT User.Username, COUNT(UserFollows.UserBeingFollowed) as FollowerCount FROM User
		LEFT JOIN UserFollows ON UserBeingFollowed = User.Username
		GROUP BY User.Username;

SELECT * FROM NumFollowers;

-- For each Username, how many people they follow that Allan also follows
CREATE OR REPLACE VIEW MutualsWithAllan AS
	SELECT User.Username, Count(UserFollows.UserFollowing) as MutualsCount FROM User
		LEFT JOIN UserFollows ON UserFollows.UserFollowing = User.Username
			AND UserFollows.UserBeingFollowed IN
				-- All people following Allan
				(SELECT UserFollowing FROM UserFollows WHERE UserBeingFollowed = "Allan")
		GROUP BY User.Username;

SELECT * FROM MutualsWithAllan;

-- Rank every user except Allan himself
SELECT * FROM User
	LEFT JOIN MutualsWithAllan ON MutualsWithAllan.Username = User.Username
	LEFT JOIN UserFollows ON UserFollows.UserBeingFollowed = "Allan" AND UserFollowing = User.Username
	LEFT JOIN NumFollowers ON NumFollowers.Username = User.Username
	WHERE User.Username != "Allan" -- Don't suggest Allan himself
	ORDER BY MutualsWithAllan.MutualsCount DESC, -- Mutuals first
	User.Username IN -- then people Allan already follows
	(SELECT UserFollowing FROM UserFollows WHERE UserBeingFollowed = "Allan") DESC,
	NumFollowers.FollowerCount DESC; -- tiebreaker who follows the most people
