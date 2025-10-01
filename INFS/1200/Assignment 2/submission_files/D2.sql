CREATE OR REPLACE VIEW NumFollowers AS
	SELECT User.Username, COUNT(UserFollows.UserBeingFollowed) as FollowerCount FROM User
		LEFT JOIN UserFollows ON UserBeingFollowed = User.Username
		GROUP BY User.Username;

-- People Allan doesn't yet follow
SELECT PotentialUser.Username FROM
	(SELECT UserBeingFollowed as Username FROM UserFollows WHERE UserBeingFollowed != "Allan"
		EXCEPT
		SELECT UserBeingFollowed FROM UserFollows WHERE UserFollowing = "Allan") as PotentialUser
	INNER JOIN NumFollowers ON NumFollowers.Username = PotentialUser.Username
	ORDER BY NumFollowers.FollowerCount DESC LIMIT 5;
