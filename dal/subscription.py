from sqlalchemy.orm import Session
from models.subscription import Subscription
from schemas.subscription_schemas import SubscriptionSchema


def get_subscriptions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Subscription).offset(skip).limit(limit).all()


def get_subscription_by_name(db: Session, name: str):
    return db.query(Subscription).filter(Subscription.name == name).first()


def create_subscription(db: Session, subscription: SubscriptionSchema):
    new_subscription = Subscription(
        name=subscription.name,
        description=subscription.description,
    )
    db.add(new_subscription)
    db.commit()
    db.refresh(new_subscription)
    return new_subscription


def delete_subscription_by_name(db: Session, name: str):
    subscription = get_subscription_by_name(db=db, name=name)
    db.delete(subscription)
    db.commit()


def update_subscription_by_name(db: Session, name: str, subscription: SubscriptionSchema):
    old_subscription = get_subscription_by_name(db=db, name=name)

    old_subscription.description = subscription.description if subscription.description else old_subscription.description

    db.commit()
    db.refresh(old_subscription)
    return old_subscription
