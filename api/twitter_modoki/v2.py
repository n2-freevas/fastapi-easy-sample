from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.param_functions import Header
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import SQLAlchemyError
from api.common.session import get_session
from service.twitter_modoki import get_tweets_by_user_id, get_tweets, get_one_tweet, post_one_tweet
from schema.response import TweetResponseModel, TweetDetailResponseModel
from schema.request import TweetRequestBodyV2   #v2で変更・追加
from api.common.authorization import required_authorization, required_header #v2で追加
from uuid import UUID
from typing import List, Optional
import traceback

twitterModokiRouter = APIRouter()


@twitterModokiRouter.get(
    '/tweet/list',
    response_model=List[TweetResponseModel],
    dependencies=[Depends(required_header), Depends(required_authorization)]
)
def 全てのツイートを取得するAPI(
    user_id: UUID = Header(...),
    offset: int = 0,
    limit: int = 100,
    session: Session= Depends(get_session)
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


@twitterModokiRouter.get('/tweet/detail', response_model=TweetDetailResponseModel, 
    #dependencies=[Depends(required_header), Depends(required_authorization)] ここにはいらない？要件定義次第だよね。
)
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

@twitterModokiRouter.post('/tweet',dependencies=[Depends(required_header), Depends(required_authorization)])
def ツイートを1つ登録するAPI(
    body: TweetRequestBodyV2,
    user_id: UUID = Header(...),
    # POSTメソッドの場合、このようにbodyに格納される予定のjsonオブジェクトの定義と結びつけると、
    # 勝手に必要な情報を構造体として抽出してくれる
    session: Session= Depends(get_session)
):
    try:
        post_one_tweet(session, body.text, user_id, body.reply_tweet_id)
        
    except BaseException as e:
        print(traceback.format_exc())
        print(e)
        if e == SQLAlchemyError:
            raise HTTPException(status_code=501, detail="Tweet Posting Error")
        else:
            raise HTTPException(status_code=500, detail="Unexpedted Error")
