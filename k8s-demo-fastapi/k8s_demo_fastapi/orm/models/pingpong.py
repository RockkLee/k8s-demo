from k8s_demo_fastapi.orm.models.base import Base
from sqlalchemy import Column, String, BigInteger, Double, DateTime


class PingPong(Base):
    __tablename__ = 'ping_pong'
    __table_args__ = {'extend_existing': True}

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    ping_msg = Column(String(255), nullable=False)
    create_date = Column(DateTime, nullable=False)