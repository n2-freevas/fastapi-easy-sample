from sqlalchemy import Column, VARCHAR, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import DateTime
from config.db_config import Base
from uuid import uuid4
from datetime import datetime

class TweetModel(Base):
    __tablename__ = "t_tweet"

    tweet_id = Column(UUID(as_uuid=True), nullable=False, default=uuid4(), primary_key=True)
    reply_tweet_id = Column(UUID(as_uuid=True))
    f_user_id = Column(ForeignKey('m_user.user_id'))
    text = Column(VARCHAR(144), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    deleted_at = Column(DateTime)
