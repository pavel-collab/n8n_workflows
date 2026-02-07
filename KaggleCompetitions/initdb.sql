-- maybe we don't need to create a database if we set an enviroment variable in docker-compose
-- CREATE DATABASE kaggle_competitions;

-- \c kaggle_competitions

create type status_type as enum ('new', 'queued', 'shown');

CREATE TABLE kaggle_competitions (title TEXT PRIMARY KEY, link TEXT NOT NULL, date_start TIMESTAMPTZ NOT NULL, deadline TIMESTAMPTZ NOT NULL, description TEXT, type TEXT, status status_type NOT NULL);
