from sqlalchemy.orm import Session
from uuid import UUID
from schema.response import TweetResponseModel, TweetDetailResponseModel
from repository import t_tweet, m_user, t_favorite

def get_tweets_by_user_id(session: Session, user_id: UUID, offset: int, limit: int):
    
    tweets = t_tweet.select_tweets_by_user_id(session, user_id, offset, limit)
    # response_modelで定義したモデルクラスを利用すると、エラーが抑えられそう。
    return [
        TweetResponseModel(
            tweet_id = t.tweet_id,
            user_name = m_user.select_user_by_user_id(session, t.f_user_id).name,
            tweet_text = t.text,
            favorites = t_favorite.count_favorite_by_tweet_id(session, t.tweet_id)
        )
        for t in tweets
    ]

def get_tweets(session: Session, offset: int, limit: int):
    
    tweets = t_tweet.select_tweets(session, offset, limit)
    return [
        TweetResponseModel(
            tweet_id = t.tweet_id,
            user_name = m_user.select_user_by_user_id(session, t.f_user_id).name,
            tweet_text = t.text,
            favorites = t_favorite.count_favorite_by_tweet_id(session, t.tweet_id)
        )
        for t in tweets
    ]

def get_one_tweet(session: Session, tweet_id: UUID):
    tweet = t_tweet.select_tweet_by_tweet_id(session, tweet_id)
    replies = t_tweet.select_reply_tweets_by_tweet_id(session, tweet_id)

    return TweetDetailResponseModel(
            tweet_id = tweet.tweet_id,
            user_name = m_user.select_user_by_user_id(session, tweet.f_user_id).name,
            tweet_text = tweet.text,
            favorites = t_favorite.count_favorite_by_tweet_id(session, tweet.tweet_id),
            reply_tweet_list = [
                TweetResponseModel(
                    tweet_id = r.tweet_id,
                    user_name = m_user.select_user_by_user_id(session, r.f_user_id).name,
                    tweet_text = r.text,
                    favorites = t_favorite.count_favorite_by_tweet_id(session, r.tweet_id),
                )
            for r in replies]
        )

def post_one_tweet(session: Session, text: str, user_id: UUID, reply_tweet_id:UUID = None):
    t_tweet.insert_tweet(session, text, user_id, reply_tweet_id)
    
        
