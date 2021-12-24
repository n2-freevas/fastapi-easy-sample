from uuid import UUID
from pydantic import BaseModel
from typing import List, Optional
from pydantic.fields import Field

# レスポンスの型と、説明と、例を定義。
class TweetRequestBody(BaseModel):
    text: str = Field(description='ツイート文', example='風邪ひいたなう')
    user_id: UUID = Field(description='ユーザのUUID', example='11112222-3333-4444-5555-666677778888')
    reply_tweet_id: Optional[UUID] = Field(description='ツイートがリプライの場合、リプライ元のツイートのIDが保存される', example='11112222-3333-4444-5555-666677778888')

class TweetRequestBodyV2(BaseModel):
    text: str = Field(description='ツイート文', example='風邪ひいたなう')
    reply_tweet_id: Optional[UUID] = Field(description='ツイートがリプライの場合、リプライ元のツイートのIDが保存される', example='11112222-3333-4444-5555-666677778888')
    