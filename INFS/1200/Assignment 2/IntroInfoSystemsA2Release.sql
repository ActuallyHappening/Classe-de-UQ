-- Database DDL DML RELEASE SET

DROP DATABASE IF EXISTS IntroInfoSystemsA2Release;
CREATE DATABASE IntroInfoSystemsA2Release;
USE IntroInfoSystemsA2Release;

-- User table
CREATE TABLE User (
    Username VARCHAR(255) PRIMARY KEY,
    Bio TEXT
);

-- Post table
CREATE TABLE Post (
    Id INT PRIMARY KEY,
    Caption TEXT,
    CreationDateTime DATETIME,
    Username VARCHAR(255),
    CONSTRAINT fk_post_user FOREIGN KEY (Username) REFERENCES User(Username)
);

-- Comment table
CREATE TABLE Comment (
    Id INT PRIMARY KEY,
    Text TEXT,
    Username VARCHAR(255),
    PostId INT,
    CONSTRAINT fk_comment_user FOREIGN KEY (Username) REFERENCES User(Username),
    CONSTRAINT fk_comment_post FOREIGN KEY (PostId) REFERENCES Post(Id)
);

-- PostImage table
CREATE TABLE PostImage (
    PostId INT,
    ImageURL VARCHAR(512),
    CONSTRAINT fk_postimage_post FOREIGN KEY (PostId) REFERENCES Post(Id),
    PRIMARY KEY (PostId, ImageURL)
);

-- UserFollows table
CREATE TABLE UserFollows (
    UserBeingFollowed VARCHAR(255),
    UserFollowing VARCHAR(255),
    PRIMARY KEY (UserBeingFollowed, UserFollowing),
    CONSTRAINT fk_userfollows_followed FOREIGN KEY (UserBeingFollowed) REFERENCES User(Username),
    CONSTRAINT fk_userfollows_following FOREIGN KEY (UserFollowing) REFERENCES User(Username)
);

-- PostReaction table
CREATE TABLE PostReaction (
    Username VARCHAR(255),
    PostId INT,
    ReactionType ENUM(
    'Like',
    'Heart',
    'CryingFaceEmoji',
    'LaughingFaceEmoji',
    'AngryReactEmoji'
    ) NOT NULL,
    PRIMARY KEY (Username, PostId),
    CONSTRAINT fk_postreaction_user FOREIGN KEY (Username) REFERENCES User(Username),
    CONSTRAINT fk_postreaction_post FOREIGN KEY (PostId) REFERENCES Post(Id)
);

INSERT INTO User (Username, Bio) VALUES
('Allan', 'A famous student at UQ who likes Operations Research.'),
('Daniel', 'A UQ tutor.'),
('Ian', 'An computer science GOAT who teaches INFS1200 course'),
('Ahuman', 'Ahuman'),
('TotallyNotABot', 'Not A Bot.');

INSERT INTO UserFollows (UserBeingFollowed, UserFollowing) VALUES
( 'Ian', 'Allan'),
( 'Daniel', 'Allan'),
( 'Ahuman', 'Allan'),
( 'Ian', 'TotallyNotABot'),
( 'Daniel', 'TotallyNotABot'),
( 'Allan', 'TotallyNotABot'),
( 'Allan', 'Daniel'),
( 'Allan', 'Ian');

INSERT INTO Post (Id, Caption, CreationDateTime, Username) VALUES
(1, 'Hey guys, please heart my awesome post', '2025-07-01 15:31:16', 'Allan'),
(2, "Ian's amazing friend at the beach.", '2025-05-15 15:37:55', 'Ian'),
(3, 'Hey guys, currently tutoring infs1200 this semester.', '2025-05-19 15:37:55', 'Allan');

INSERT INTO PostReaction (Username, PostId, ReactionType) VALUES
('Allan', 1, 'Heart'),
('Ian', 1, 'Heart'),
('Daniel', 1, 'Heart');

INSERT INTO PostImage (PostId, ImageURL) VALUES
(2, 'https://antisocial.media/a3b8c9d4-e5f6-4a7b-8c9d-1e2f3a4b5c6d.png');

INSERT INTO Comment (Id, Text, Username, PostId) VALUES
(1, 'This is quite fascinating. A really beautiful story.', 'Ian', 2),
(2, 'Legendary!!', 'Allan', 2),
(3, "That's awsesome", 'Daniel', 1);
