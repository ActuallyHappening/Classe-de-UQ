CREATE TABLE Message (
	Id INT PRIMARY KEY,
	Sender VARCHAR(255) NOT NULL,
	Receiver VARCHAR(255) NOT NULL,
	Message VARCHAR(512),
	IntegrityHash CHAR(64)
		-- AS (SHA2((SELECT Id, Sender, Receiver, Message), 256)),
		COMMENT "I'm not sure if we are supposed to auto-generate this" UNIQUE,

	CONSTRAINT no_self_messages CHECK (Sender != Receiver),
	CONSTRAINT fk_message_sender FOREIGN KEY (Sender) REFERENCES User(Username),
	CONSTRAINT fk_message_receiver FOREIGN KEY (Receiver) REFERENCES User(Username)
)
