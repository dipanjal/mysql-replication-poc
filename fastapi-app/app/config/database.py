import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_config_map = {
    "HOST": os.getenv("DB_HOST"),
    "PORT": os.getenv("DB_PORT"),
    "NAME": os.getenv("DB_NAME"),
    "USER": os.getenv("DB_USER"),
    "PASSWORD": os.getenv("DB_PASSWORD"),
}

def get_db_url():
    for key, value in db_config_map.items():
        if not value:
            raise RuntimeError(f"DB_{key} is not set")
    return f"mysql+pymysql://{db_config_map['USER']}:{db_config_map['PASSWORD']}@{db_config_map['HOST']}:{db_config_map['PORT']}/{db_config_map['NAME']}"

engine = create_engine(
    get_db_url(),
    echo=False,
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
