-- All followers
SELECT UserFollowing FROM UserFollows
    WHERE UserBeingFollowed = "Allan"
EXCEPT
-- All people who HAVE reacted to the most recent post
SELECT UserFollowing FROM UserFollows
	INNER JOIN Post as MostRecentPost ON MostRecentPost.CreationDateTime = (SELECT MAX(CreationDateTime) FROM Post WHERE Username = "Allan")
	INNER JOIN PostReaction ON PostReaction.PostId = MostRecentPost.Id
    AND PostReaction.Username = UserFollows.UserFollowing
    WHERE UserBeingFollowed = "Allan"
