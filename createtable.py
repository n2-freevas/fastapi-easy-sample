from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session
from config.db_config import engine1
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime
from sqlalchemy.sql.sqltypes import DateTime,VARCHAR
from sqlalchemy.types import DateTime
from sqlalchemy.orm import relationship
from config.db_config import SessionLocal


Base_for_create_table = declarative_base()

class UserModel(Base_for_create_table):
    __tablename__ = "m_user"

    user_id = Column(UUID(as_uuid=True), nullable=False, default=uuid4(), primary_key=True)
    name = Column(VARCHAR(32), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    deleted_at = Column(DateTime)

    tweet = relationship("TweetModel")
    favorite = relationship("FavoriteModel")

class TweetModel(Base_for_create_table):
    __tablename__ = "t_tweet"

    tweet_id = Column(UUID(as_uuid=True), nullable=False, default=uuid4(), primary_key=True)
    reply_tweet_id = Column(UUID(as_uuid=True))
    f_user_id = Column(ForeignKey('m_user.user_id'))
    text = Column(VARCHAR(144), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    deleted_at = Column(DateTime)
    
    favorite = relationship("FavoriteModel")


class FavoriteModel(Base_for_create_table):
    __tablename__ = "t_favorite"

    favorite_id = Column(UUID(as_uuid=True), nullable=False, default=uuid4(), primary_key=True)
    f_tweet_id = Column(ForeignKey('t_tweet.tweet_id'))
    f_user_id = Column(ForeignKey('m_user.user_id'))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    deleted_at = Column(DateTime)

Base_for_create_table.metadata.create_all(bind=engine1)

session :Session = SessionLocal()
user1 = UserModel(
    user_id = '12341234-1234-1234-1234-123412341234',
    name = 'へんぴなユーザ',
)
user2 = UserModel(
    user_id = '43214321-4321-4321-4321-432143214321',
    name = 'JKのフリしたおっさん',
)
tweet1 = TweetModel(
    tweet_id = '11111111-1111-1111-1111-111111111111',
    f_user_id = '12341234-1234-1234-1234-123412341234',
    text = 'ハーゲンダッツって高級感の割に300円てマ？'
)
tweet2 = TweetModel(
    tweet_id = '11111111-1111-1111-1111-111111111112',
    f_user_id = '43214321-4321-4321-4321-432143214321',
    text = '犬ってゅうのゎ。。\n英語で「dog」\n逆から読むと。。\n「god」\nそぅ神。。\nぃみゎかんなぃ。。。。\nもぅﾏﾁﾞ無理。'
)

tweet3 = TweetModel(
    tweet_id = '11111111-1111-1111-1111-111111111113',
    reply_tweet_id = '11111111-1111-1111-1111-111111111112',
    f_user_id = '12341234-1234-1234-1234-123412341234',
    text = '意味不明すぎて草'
)
favorite1 = FavoriteModel(
    favorite_id = '99999999-9999-9999-9999-999999999999',
    f_tweet_id = '11111111-1111-1111-1111-111111111112',
    f_user_id = '12341234-1234-1234-1234-123412341234'
)


session.add(user1)
session.add(user2)
session.add(tweet1)
session.add(tweet2)
session.add(tweet3)
session.add(favorite1)
session.commit()
