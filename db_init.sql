CREATE TABLE guilds (
    guild_id integer PRIMARY KEY
);

CREATE TABLE users (
    user_id integer PRIMARY KEY,
    guild_id integer REFERENCES guilds(guild_id)
);

CREATE TABLE logs (
    log_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    log_type text,
    unix_timestamp integer,
    guild_id integer REFERENCES guilds(guild_id),
    user_id integer REFERENCES users(user_id)
);