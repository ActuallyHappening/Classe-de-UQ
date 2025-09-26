CREATE TABLE UserCreatesPost (
	Username VARCHAR(255),
	PostId INT,
	PRIMARY KEY (Username, PostId),

	PersonalNote TEXT,

	CONSTRAINT fk_ucp_username FOREIGN KEY (Username) REFERENCES User(Username),
	CONSTRAINT fk_ucp_post_id FOREIGN KEY (PostId) REFERENCES Post(Id),
)
