import validators
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from starlette.datastructures import URL

from . import models, schemas, crud, config
from .database import engine, get_db

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def bad_request(message: str):
    raise HTTPException(status_code=400, detail=message)


def get_url_info(link: models.Url) -> schemas.UrlInfo:
    base_url = URL(config.config().base_url)
    return schemas.UrlInfo(
        target_url=link.target_url,
        clicks=link.clicks,
        url=str(base_url.replace(path=link.short_id)),
        admin_url=str(base_url.replace(path=f"{link.short_id}/{link.secret}")),
    )


@app.get("/")
def home(db: Session = Depends(get_db)):
    return [get_url_info(x) for x in db.query(models.Url).all()]


@app.post("/url", response_model=schemas.UrlInfo)
def create(url: schemas.UrlBase, db: Session = Depends(get_db)) -> schemas.UrlInfo:
    if not validators.url(url.target_url):
        bad_request(message="Invalid URL")

    return get_url_info(crud.insert_url(db, url.target_url))


@app.get("/{short_id}")
def redirect(short_id: str, request: Request, db: Session = Depends(get_db)):
    link = crud.get_url_by_short_id(db, short_id)
    if link:
        crud.update_clicks(db=db, link_id=link.id)
        return RedirectResponse(link.target_url)

    raise HTTPException(status_code=404)


@app.get("/info/{short_id}", response_model=schemas.UrlInfo)
def info(short_id: str, db: Session = Depends(get_db)):
    link = crud.get_url_by_short_id(db, short_id)
    if link:
        return get_url_info(link)

    raise HTTPException(status_code=404)


@app.delete("/{short_id}/{secret}")
def delete(short_id: str, secret: str, db: Session = Depends(get_db)):
    link = crud.find_by_secret(db, short_id, secret)
    if link:
        crud.delete(db, link.id)
        return {"success": True}

    raise HTTPException(status_code=404)
