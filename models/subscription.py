from sqlalchemy import Column, String

from config.db import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    name = Column(String, primary_key=True, nullable=False)
    description = Column(String, nullable=False)
