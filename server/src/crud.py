import secrets
import string

from sqlalchemy.orm import Session
from sqlalchemy.sql import exists

from . import models, config


def random_id(max_len: int = 5) -> str:
    return "".join(
        secrets.choice(string.ascii_letters + string.digits) for _ in range(max_len)
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


def delete(db: Session, id: int):
    db.query(models.Url).filter(models.Url.id == id).delete()
    db.commit()


def find_by_secret(db: Session, short_id: str, secret: str) -> models.Url:
    return (
        db.query(models.Url)
        .filter(models.Url.short_id == short_id, models.Url.secret == secret)
        .first()
    )


def update_clicks(db: Session, link_id: int):
    db.query(models.Url).filter_by(id=link_id).update({"clicks": models.Url.clicks + 1})
    db.commit()


def insert_url(db: Session, target_url: str) -> models.Url:
    short_id = generate_unique_short_id(db, config.config().short_id_length)
    secret = random_id(config.config().secret_length)
    link = models.Url(target_url=target_url, short_id=short_id, secret=secret)
    db.add(link)
    db.commit()
    db.refresh(link)
    return link
