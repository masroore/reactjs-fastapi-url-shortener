from pydantic import BaseModel


class UrlBase(BaseModel):
    target_url: str


class Url(UrlBase):
    short_id: str
    secret: str
    is_active: bool
    clicks: int

    class Config:
        orm_mode = True


class UrlInfo(UrlBase):
    clicks: int
    url: str
    delete_url: str
