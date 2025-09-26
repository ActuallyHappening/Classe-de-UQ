SELECT NotIanUser.Username
	FROM User as UserIan
	INNER JOIN User as NotIanUser ON NotIanUser.Username != "Ian"
    INNER JOIN Comment as IanComment ON IanComment.Username = "Ian"
    INNER JOIN Post as IanCommentedOnPost ON IanComment.PostId = IanCommentedOnPost.Id
    INNER JOIN Comment as NotIanComment ON NotIanComment.Username = NotIanUser.Username AND NotIanComment.PostId = IanCommentedOnPost.Id
    WHERE UserIan.Username = "Ian"