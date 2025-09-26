INSERT INTO Post VALUES ROW(200, "New pics from Japan!", "2025-07-10 2:53", "Allan");

INSERT INTO PostImage VALUES ROW(200, "https://antisocial.media/2c3d4e5f-6a7b-48c9-d1e2-f3a4b5c6d7e8.jpg");
INSERT INTO PostImage VALUES ROW(200, "https://antisocial.media/f1e2d3c4-b5a6-4978-9182-3d4e5f6a7b8c.png");

INSERT INTO PostReaction SELECT Username, 200 as PostId, "Like" as ReactionType FROM User WHERE Username != "Allan";
