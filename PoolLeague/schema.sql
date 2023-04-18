DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS game;

CREATE TABLE player (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name STRING UNIQUE NOT NULL,
    email STRING -- Currently unused. Might be fun to email with league position updates.
);

-- Not storing game scores in the db because they can be easily reconstructed.
CREATE TABLE game (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL DEFAULT CURRENT_DATE,
    red_player_id INTEGER NOT NULL,
    yellow_player_id INTEGER NOT NULL,
    reds_potted INTEGER NOT NULL,
    yellows_potted INTEGER NOT NULL,
    winner_id INTEGER NOT NULL, -- Bit redundant storing the winner id rather than a boolean for player1/2; this makes calculating scores simpler though.
    FOREIGN KEY (red_player_id) REFERENCES user (id),
    FOREIGN KEY (yellow_player_id) REFERENCES user (id),
    FOREIGN KEY (winner_id) REFERENCES user (id)
);