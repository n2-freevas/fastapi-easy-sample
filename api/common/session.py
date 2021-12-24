from sqlalchemy.orm import Session
from config.db_config import SessionLocal

# セッションを一旦停止して返す共通関数
def get_session():
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        
