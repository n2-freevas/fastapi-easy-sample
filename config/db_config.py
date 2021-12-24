from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine1 = create_engine(
    "ここにURI入れてね・postgres > postgresql にしてね"
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine1)

Base = declarative_base()

