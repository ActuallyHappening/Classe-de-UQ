CREATE TABLE UserCreatesPost (
	Username VARCHAR(255),
	PostId INT,
	PersonalNote TEXT,

	PRIMARY KEY (Username, PostId),
	CONSTRAINT fk_ucp_username FOREIGN KEY (Username) REFERENCES User(Username),
	CONSTRAINT fk_ucp_post_id FOREIGN KEY (PostId) REFERENCES Post(Id)
);

INSERT INTO UserCreatesPost (Username, PostId, PersonalNote)
	SELECT Post.Username, Post.Id, CONCAT(Post.Username, ": ", Post.Caption) FROM Post;

ALTER TABLE Post DROP CONSTRAINT fk_post_user, DROP COLUMN Username;
