Подготовка docker-compose

```
docker compose up --build
```

После старта всех контейнеров доступ можно будет получить на хостах
```
# n8n
http://localhost:5678

# fast api
http://localhost:8000/health
```

Для того, чтобы дернуть ручку для получения списка соревнований:
```
http://localhost:8000/competitions
```

Подготовка базы данных PostgreSQL
```
CREATE DATABASE kaggle_competitions;

create type status_type as enum ('new', 'queued', 'shown');
```

```
CREATE TABLE kaggle_competitions (title TEXT PRIMARY KEY, link TEXT NOT NULL, date_start TIMESTAMPTZ NOT NULL, deadline TIMESTAMPTZ NOT NULL, status status_type NOT NULL);
```

Добавление новой записи
```
INSERT INTO kaggle_competitions (title, link, date_start, deadline, status) VALUES ('', '', '', '', 'new');
```

Извлечение записей из бд
```
SELECT * FROM kaggle_competitions WHERE status = 'new' OR status = 'queued' ORDER BY deadline LIMIT 10;
```

Модификация вставленных записей
```
UPDATE kaggle_competitions SET status = 'shown' WHERE title = '';
```
