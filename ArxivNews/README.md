Запуск сервиса n8n
```
docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

Кроме того должен быть поднят сервис PostgreSQL. 

ATTENTION: обратите внимание, что при первичной инициализации docker volume (для postgresql) происходит настройка базы и таблицы с использованием скрипта initdb.sql. Эта настройка происходит только при первичной инициализации volume. Так что если вы меняете скрипт initdb.sql необходимо удалить volume базы postgresql и стартовать docker-compose.

### Настройка базы данных и таблицы
```
CREATE DATABASE arxiv_records;

create type status_type as enum ('new', 'queued', 'shown');

CREATE TABLE arxiv_records (title text primary key, link text, author text, pub_date timestamptz not null, summary text not null, status status_type not null);
```

Виды запросов к бд

Вставка данных
```
insert into arxiv_records (title, link, author, pub_date, summary, status) values ('', '', '', '', '', 'new') on conflict (title) do nothing;
```

Извлечение данных
```
select * from arxiv_records where status = 'new' or status = 'queued' limit 5;
```

Обновление данных
```
update arxiv_records set status = 'shown'  where title = 'Almost all standard double covers of abelian Cayley graphs have smallest possible automorphism groups';
```
