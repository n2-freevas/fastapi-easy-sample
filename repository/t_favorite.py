from uuid import UUID
from sqlalchemy.orm.session import Session
from model.FavoriteModel import FavoriteModel

def count_favorite_by_tweet_id(
        session: Session, tweet_id: UUID
    )->int:
    return (
        session.query(FavoriteModel)
        .filter(FavoriteModel.f_tweet_id == tweet_id)
        .count() # 条件にあう、数を数える
    )
