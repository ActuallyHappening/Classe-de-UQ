-- Number of followers by username
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
				-- All people who Allan follows
				(SELECT UserBeingFollowed FROM UserFollows WHERE UserFollowing = "Allan")
		GROUP BY User.Username;

SELECT * FROM MutualsWithAllan;

-- The people who follow Allan
SELECT UserFollowing FROM UserFollows WHERE UserBeingFollowed = "Allan";
-- The people who Allan follows
SELECT UserBeingFollowed FROM UserFollows WHERE UserFollowing = "Allan";

-- Rank every user except Allan himself
SELECT User.Username, User.Bio,
	User.Username IN
		(SELECT UserFollowing FROM UserFollows WHERE UserBeingFollowed = "Allan")
	as AllanFollows,
MutualsCount, FollowerCount FROM User
	LEFT JOIN MutualsWithAllan ON MutualsWithAllan.Username = User.Username
	LEFT JOIN NumFollowers ON NumFollowers.Username = User.Username
	WHERE User.Username != "Allan" -- Don't ever suggest Allan himself
	ORDER BY
		User.Username IN -- prioritise if user follows Allan
		(SELECT UserFollowing FROM UserFollows WHERE UserBeingFollowed = "Allan") DESC,
		MutualsWithAllan.MutualsCount DESC, -- Mutuals first
		NumFollowers.FollowerCount DESC, -- tiebreaker who follows the most people
		User.Username
	LIMIT 5;
