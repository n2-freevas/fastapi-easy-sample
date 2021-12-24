from uuid import UUID
from sqlalchemy.orm.session import Session
from model.UserModel import UserModel
from sqlalchemy.orm.exc import NoResultFound

# ユーザIDを指定して、そのユーザがツイートしたツイートの一覧を返す
def select_user_by_user_id(
        session: Session, user_id: UUID
    )->UserModel:
    try:
        return (
            session.query(UserModel)
            .filter(UserModel.user_id == user_id)
            .one()
        )
    except NoResultFound as e:
        raise e
