from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import SQLAlchemyError
from api.common.session import get_session
from service.twitter_modoki import get_tweets_by_user_id, get_tweets, get_one_tweet, post_one_tweet
from schema.response import TweetResponseModel, TweetDetailResponseModel
from schema.request import TweetRequestBody
from uuid import UUID
from typing import List, Optional
import traceback

twitterModokiRouter = APIRouter()

# .(メソッド名) ('{パス}', response_model={レスポンスの形式})
@twitterModokiRouter.get('/tweet/list', response_model=List[TweetResponseModel])
def 全てのツイートを取得するAPI( # APIの関数名が、自動生成ドキュメントのAPIの説明文になります。
    user_id: UUID = None, # クエリパラメータ。 型チェック(もしくは変換)・軽いバリデーションもしてくれる
    offset: int = 0,    # クエリパラメータ, デフォルト値を設定すると自動的にOptionalになる。
    limit: int = 100,   # クエリパラメータ
    session: Session= Depends(get_session)  # APIの開始時にget_sessionが呼び出され、終了時にはget_sessionのfinallyを実行する。
):
    try:
        if(user_id):
            data = get_tweets_by_user_id(session,user_id, offset, limit)
            
        else:
            data = get_tweets(session, offset, limit)

        return jsonable_encoder(data)

    # BaseExceptionで全てのエラーを検知し、内容によって色々分ける
    except BaseException as e:
        print(traceback.format_exc())
        print(e)
        raise HTTPException(status_code=500, detail="Unexpedted Error")


@twitterModokiRouter.get('/tweet/detail', response_model=TweetDetailResponseModel)
def ツイートを1つ取得するAPI(
    tweet_id: UUID,
    session: Session= Depends(get_session)
):
    try:
        data = get_one_tweet(session, tweet_id)
        return jsonable_encoder(data)

    except BaseException as e:
        print(traceback.format_exc())
        print(e)
        if e == NoResultFound:
            raise HTTPException(status_code=404, detail="The tweet is Not Found")
        else:
            raise HTTPException(status_code=500, detail="Unexpedted Error")

@twitterModokiRouter.post('/tweet')
def ツイートを1つ登録するAPI(
    body: TweetRequestBody, 
    # POSTメソッドの場合、このようにbodyに格納される予定のjsonオブジェクトの定義と結びつけると、
    # 勝手に必要な情報を構造体として抽出してくれる
    session: Session= Depends(get_session)
):
    try:
        post_one_tweet(session, body.text, body.user_id, body.reply_tweet_id)
        
    except BaseException as e:
        print(traceback.format_exc())
        print(e)
        if e == SQLAlchemyError:
            raise HTTPException(status_code=501, detail="Tweet Posting Error")
        else:
            raise HTTPException(status_code=500, detail="Unexpedted Error")
