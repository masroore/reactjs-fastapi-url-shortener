import validators
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, get_db

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def bad_request(message: str):
    raise HTTPException(status_code=400, detail=message)


def not_found(request: Request):
    message = f"URL '{request.url}' doesn't exist"
    raise HTTPException(status_code=404, detail=message)


@app.get("/")
def home(db: Session = Depends(get_db)):
    return db.query(models.Url).all()


@app.post("/url", response_model=schemas.Url)
def create(url: schemas.UrlBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        bad_request(message="Invalid URL")

    return crud.insert_url(db, url.target_url)


@app.get("/{short_id}")
def redirect(short_id: str, request: Request, db: Session = Depends(get_db)):
    link = crud.get_url_by_short_id(db, short_id)
    if link:
        crud.update_clicks(db=db, link=link)
        return RedirectResponse(link.target_url)

    raise HTTPException(status_code=404)


@app.delete("/{short_id}/{secret}")
def delete(short_id: str, secret: str, db: Session = Depends(get_db)):
    if crud.delete_short_id(db, short_id, secret):
        return {"success": True}

    raise HTTPException(status_code=404)
