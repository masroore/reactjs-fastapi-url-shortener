import secrets
import string

from sqlalchemy.orm import Session
from sqlalchemy.sql import exists, delete

from . import models, config


def random_id(max_len: int = 5) -> str:
    return "".join(
        secrets.choice(string.ascii_uppercase + string.digits) for _ in range(max_len)
    )


def generate_unique_short_id(db: Session, max_len: int = 5) -> str:
    short_id = random_id(max_len)

    while short_id_exists(db, short_id):
        short_id = random_id(max_len)

    return short_id


def get_url_by_short_id(db: Session, short_id: str) -> models.Url | None:
    return (
        db.query(models.Url)
        .filter(models.Url.short_id == short_id, models.Url.is_active == True)
        .first()
    )


def short_id_exists(db: Session, short_id: str) -> bool:
    return db.query(exists().where(models.Url.short_id == short_id)).scalar()
    # return db.query(models.Url).filter(models.Url.short_id == short_id).count() > 0


def delete_short_id(db: Session, short_id: str, secret: str) -> bool:
    return db.query(
        delete().where(models.Url.short_id == short_id, models.Url.secret == secret)
    ).scalar()


def update_clicks(db: Session, link: models.Url) -> models.Url:
    link.clicks += 1
    db.commit()
    db.refresh(link)
    return link


def insert_url(db: Session, target_url: str) -> models.Url:
    short_id = generate_unique_short_id(db, config.config().short_id_length)
    secret = random_id(config.config().secret_length)
    link = models.Url(target_url=target_url, short_id=short_id, secret=secret)
    db.add(link)
    db.commit()
    db.refresh(link)
    return link
