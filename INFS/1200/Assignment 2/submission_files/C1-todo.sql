CREATE TABLE Message (
	Id INT PRIMARY KEY,
	Sender VARCHAR(255),
	Receiver VARCHAR(255),
	Message TEXT,
	IntegrityHash VARCHAR(64) UNIQUE,
	-- TODO Integrity computed

	CONSTRAINT fk_message_sender FOREIGN KEY (Sender) REFERENCES User(Username),
	CONSTRAINT fk_message_receiver FOREIGN KEY (Receiver) REFERENCES User(Username)
)
