SELECT PostId, COUNT(*) FROM PostReaction WHERE ReactionType = "heart" GROUP BY PostId HAVING COUNT(*) >= 3
