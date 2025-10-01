SELECT NotIanUser.Username
	FROM User as UserIan
	INNER JOIN User as NotIanUser ON 1
		-- ON NotIanUser.Username != "Ian"
		-- confusingly, the question clearly states "The username Iam should be returned in this result",
		-- which I take to meaning Ian should always be returned
    INNER JOIN Comment as IanComment ON IanComment.Username = "Ian"
    INNER JOIN Post as IanCommentedOnPost ON IanComment.PostId = IanCommentedOnPost.Id
    INNER JOIN Comment as NotIanComment ON NotIanComment.Username = NotIanUser.Username AND NotIanComment.PostId = IanCommentedOnPost.Id
    WHERE UserIan.Username = "Ian";
