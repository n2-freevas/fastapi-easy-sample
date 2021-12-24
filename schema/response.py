from uuid import UUID
from pydantic import BaseModel
from typing import List, Optional
from pydantic.fields import Field

# レスポンスの型と、説明と、例を定義。
class TweetResponseModel(BaseModel):
    tweet_id: UUID = Field(description='ツイートのUUID', example='12341234-1234-1234-1234-123412341234')
    user_name: str = Field(description='ツイート主の名前', example='ユーザ1')
    tweet_text: str = Field(description='ツイート内容', example='Twitter Modoki!')
    favorites: int = Field(description='いいね数', example=10)

#継承も可
class TweetDetailResponseModel(TweetResponseModel):
    reply_tweet_list: List[TweetResponseModel] = Field(description='リプライがあればリプライの一覧が格納', example=[])
