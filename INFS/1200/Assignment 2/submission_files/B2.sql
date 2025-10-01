-- attribute to daniel
UPDATE Comment SET Username = "Daniel" WHERE Username = "TotallyNotABot";
UPDATE PostReaction SET Username = "Daniel" WHERE Username = "TotallyNotABot";
UPDATE Post SET Username = "Daniel" WHERE Username = "TotallyNotABot";

-- remove any bot following/being followed
DELETE FROM UserFollows WHERE UserBeingFollowed = "TotallyNotABot" OR UserFollowing = "TotallyNotABot";

-- finally remove user
DELETE FROM User WHERE Username = "TotallyNotABot";
