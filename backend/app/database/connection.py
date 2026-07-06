import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from app.config.settings import settings

Base = declarative_base()
SessionLocal = None
engine = None


def build_database_url():
    user = settings.DATABASE_USER
    password = urllib.parse.quote_plus(settings.DATABASE_PASSWORD)
    host = settings.DATABASE_HOST
    port = settings.DATABASE_PORT
    db = settings.DATABASE_NAME
    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8mb4"


def init_engine(settings_obj=None):
    global engine, SessionLocal
    if settings_obj is None:
        from app.config.settings import settings as settings_obj
    url = build_database_url()
    engine = create_engine(url, pool_pre_ping=True, future=True)
    SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    return engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
