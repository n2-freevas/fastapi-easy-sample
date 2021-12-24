from fastapi import Header, HTTPException
from sqlalchemy.orm.session import Session
from model.UserModel import UserModel
from config.db_config import SessionLocal
from uuid import UUID

def required_authorization(
        authorization: str = Header(...)
    ):
    if authorization == 'fast-api-token-barebare':
        pass
    else:
        #キーが違うなら、リクエストをRejectする。
        raise HTTPException(status_code=432, detail="Access invalid")

def required_header(
        user_id: UUID = Header(...)
    ):
    session: Session = SessionLocal()
    try:
        #get()によって、該当するidをもつユーザが0つ、あるいは2つ以上取れた時、エラーを吐く。
        session.query(UserModel).get(user_id)
    except:
        #ので、リクエストをRejectできる。
        raise HTTPException(status_code=432, detail="Access invalid")
    finally:
        session.close()
