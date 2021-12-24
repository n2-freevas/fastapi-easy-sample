from typing import List
from uuid import UUID, uuid4
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import desc
from model.TweetModel import TweetModel
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import SQLAlchemyError

# ユーザIDを指定して、そのユーザがツイートしたツイートの一覧を返す
def select_tweets_by_user_id(
        session: Session, user_id:int, offset:int, limit:int
    )->List[TweetModel]:
    
    #SQLAlchemyを使って、DBから情報を取り出す。
    #fastapiと関係ないので、詳細な説明は省略
    return ( session.query(TweetModel)
        .filter(TweetModel.f_user_id == user_id) #ユーザのIDを絞り込み
        .order_by(desc(TweetModel.created_at)) #新しい順にソート
        .offset(offset) # 上から何番目からとるか
        .limit(limit) # offsetスタートで、何個とるか
        .all() #↑の条件を満たすアイテム全て取得
    )
    
def select_tweets(
        session: Session, offset:int, limit:int
    )->List[TweetModel]:
    
    return ( session.query(TweetModel)
        .order_by(desc(TweetModel.created_at))
        .offset(offset)
        .limit(limit)
        .all()
    )

def select_tweet_by_tweet_id(
        session: Session, tweet_id: UUID,
    )->TweetModel:
    try:
        return (
            session.query(TweetModel)
            .filter(TweetModel.tweet_id == tweet_id)
            .one()
        )
    except NoResultFound as e:
        raise e

def select_reply_tweets_by_tweet_id(
    session: Session, tweet_id: UUID
)->List[TweetModel]:
    return (
        session.query(TweetModel)
        .filter(TweetModel.reply_tweet_id == tweet_id)
        .order_by(desc(TweetModel.created_at))
        .all()
    )


def insert_tweet(
    session: Session, text: str, user_id: UUID, reply_tweet_id:UUID = None
):
    try:
        tweet = TweetModel(
            tweet_id = uuid4(),
            reply_tweet_id = reply_tweet_id,
            f_user_id = user_id,
            text = text,
        )
        session.add(tweet)
        session.commit()
        # DBに反映する処理は、session.commit()か、flush()の2つ。
        # 前者は変更を確定するもの、
        # 後者はORM上で変更を確定し、DBには反映しないもの。
        # flush()での変更は、session.rollback()で、取り消せるし、
        # flush()でたまった変更は、commit()でまとめてDBに反映できる。
    except SQLAlchemyError as e:
        #session.rollback()
        raise e
