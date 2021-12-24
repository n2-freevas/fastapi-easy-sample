from sqlalchemy import Column, VARCHAR
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import DateTime
from config.db_config import Base
from uuid import uuid4
from datetime import datetime

class UserModel(Base):
    __tablename__ = "m_user"

    user_id = Column(UUID(as_uuid=True), nullable=False, default=uuid4(), primary_key=True)
    name = Column(VARCHAR(32), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    deleted_at = Column(DateTime)
