from fastapi import FastAPI
from kaggle.api.kaggle_api_extended import KaggleApi
from datetime import datetime, timedelta
from typing import List, Dict

app = FastAPI(title="Kaggle Competitions API")

MAX_PAGE_NUMBER = 10
PAGE_SIZE = 100


def get_active_competitions() -> List[Dict]:
    api = KaggleApi()
    api.authenticate()

    competitions = []
    page = 1
    today_date = datetime.now()

    while True:
        comps = api.competitions_list(
            page=page,
            page_size=PAGE_SIZE,
            search="",
            category="all",
            sort_by="latestDeadline",
        )

        if not comps or not comps.competitions:
            break

        for c in comps.competitions:
            deadline_date = c.deadline

            # только активные
            if deadline_date < today_date:
                continue

            # минимум 7 дней до дедлайна
            if deadline_date - today_date < timedelta(days=7):
                continue

            competitions.append(c)

        page += 1
        if page >= MAX_PAGE_NUMBER:
            break

    result = []
    for c in competitions:
        description = c.description or ""
        description += "\n\n".join(
            tag.description for tag in c.tags if tag.description
        )

        tags = ", ".join(tag.ref for tag in c.tags if tag.ref)

        result.append(
            {
                "competition_title": c.title,
                "link": c.ref,
                "date_start": c.enabled_date.strftime("%Y-%m-%d"),
                "deadline": c.deadline.strftime("%Y-%m-%d"),
                "description": description,
                "tags": tags,
            }
        )

    return result


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/competitions")
def competitions():
    data = get_active_competitions()
    return {
        "count": len(data),
        "items": data,
    }

