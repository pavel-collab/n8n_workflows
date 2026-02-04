-- maybe we don't need to create a database if we set an enviroment variable in docker-compose
-- CREATE DATABASE arxiv_records;

-- \c arxiv_records

create type status_type as enum ('new', 'queued', 'shown');

CREATE TABLE arxiv_records (title text primary key, link text, author text, pub_date timestamptz not null, summary text not null, status status_type not null);
