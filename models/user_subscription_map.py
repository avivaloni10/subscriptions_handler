import datetime

from sqlalchemy import Column, String, ForeignKey, DateTime

from config.db import Base


class UserSubscriptionMap(Base):
    __tablename__ = "user_subscription_map"

    subscription_name = Column(ForeignKey("subscriptions.name"), primary_key=True, nullable=False)
    user_email = Column(ForeignKey("users.email"), primary_key=True, nullable=False)
    card_owner_id = Column(String, nullable=False)
    card_number = Column(String, nullable=False)
    cvv = Column(String, nullable=False)
    start_date = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    expiration_date = Column(DateTime, default=(datetime.datetime.now() + datetime.timedelta(6 * 30)), nullable=False)
