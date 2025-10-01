-- Counting reactions to any of Allan's posts by username
CREATE OR REPLACE VIEW AllanReactions AS
	SELECT User.Username, COUNT(PostReaction.Username) as ReactionsCount FROM User
	--  LEFT so that if no matching post reactions exist, counts as 0
		LEFT JOIN PostReaction ON PostReaction.PostId = Post.Id,
		INNER JOIN Post ON Post.Username = "Allan"
		WHERE PostReaction.Username = User.Username
		GROUP BY User.Username;

SELECT * FROM AllanReactions;

-- Counting comments to any of Allan's posts by username
CREATE OR REPLACE VIEW AllanComments AS
	SELECT User.Username, COUNT(Comment.Username) as CommentsCount FROM User
	--  LEFT so that if no matching comments exist, counts as 0
		LEFT JOIN Comment ON Comment.Username = User.Username
		INNER JOIN Post ON Post.Username = "Allan" AND Comment.PostId = Post.Id
		GROUP BY User.Username;

SELECT * FROM AllanComments;

SELECT COUNT(UserFollows.UserFollowing) FROM UserFollows
	INNER JOIN AllanReactions ON AllanReactions.Username = UserFollows.UserFollowing
	INNER JOIN AllanComments ON AllanComments.Username = UserFollows.UserFollowing
	WHERE UserFollows.UserBeingFollowed = "Allan"
		AND AllanReactions.ReactionsCount >= 1
		AND AllanComments.CommentsCount = 0;
