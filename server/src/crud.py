from sqlalchemy.orm import Session
from sqlalchemy.sql import exists
from starlette.datastructures import URL

from . import models, config, schemas, utils


def generate_unique_short_id(db: Session, max_len: int = 5) -> str:
    short_id = utils.generate_random_id(max_len)

    while short_id_exists(db, short_id):
        short_id = utils.generate_random_id(max_len)

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


def delete_url(db: Session, id: int):
    db.query(models.Url).filter(models.Url.id == id).delete()
    db.commit()


def find_by_secret(db: Session, short_id: str, secret: str) -> models.Url:
    return (
        db.query(models.Url)
        .filter(models.Url.short_id == short_id, models.Url.secret == secret)
        .first()
    )


def find_by_target_url(db: Session, target_url: str) -> models.Url:
    return db.query(models.Url).filter(models.Url.target_url == target_url).first()


def update_clicks(db: Session, link_id: int):
    db.query(models.Url).filter_by(id=link_id).update({"clicks": models.Url.clicks + 1})
    db.commit()


def insert_url(db: Session, target_url: str) -> models.Url:
    target_url = utils.normalize_url(target_url)
    link = find_by_target_url(db, target_url)
    if link:
        return link

    short_id = generate_unique_short_id(db, config.config().short_id_length)
    secret = utils.generate_random_id(config.config().secret_length)
    link = models.Url(target_url=target_url, short_id=short_id, secret=secret)
    db.add(link)
    db.commit()
    db.refresh(link)
    return link


def get_url_info(link: models.Url) -> schemas.UrlInfo:
    base_url = URL(config.config().base_url)
    return schemas.UrlInfo(
        target_url=link.target_url,
        clicks=link.clicks,
        url=str(base_url.replace(path=link.short_id)),
        delete_url=str(base_url.replace(path=f"{link.short_id}/{link.secret}")),
    )
