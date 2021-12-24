from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Boolean, DateTime
from config.db_config import Base
from uuid import uuid4
from datetime import datetime

class FavoriteModel(Base):
    __tablename__ = "t_favorite"

    favorite_id = Column(UUID(as_uuid=True), nullable=False, default=uuid4(), primary_key=True)
    f_tweet_id = Column(ForeignKey('t_tweet.tweet_id'))
    f_user_id = Column(ForeignKey('m_user.user_id'))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    deleted_at = Column(DateTime)
