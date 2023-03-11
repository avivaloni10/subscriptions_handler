from sqlalchemy.orm import Session
from models.user_subscription_map import UserSubscriptionMap
from schemas.user_subscription_map_schemas import UserSubscriptionMapSchema


def get_user_subscription_maps(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserSubscriptionMap).offset(skip).limit(limit).all()


def get_user_subscriptions_user_email(db: Session, user_email: str):
    return db.query(UserSubscriptionMap).filter(UserSubscriptionMap.user_email == user_email).first()


def get_subscription_users_by_subscription_name(db: Session, subscription_name: str):
    return db.query(UserSubscriptionMap).filter(UserSubscriptionMap.subscription_name == subscription_name).first()


def get_user_subscription_map_by_user_email_subscription_name(db: Session, user_email: str, subscription_name: str):
    return db.query(UserSubscriptionMap).filter(UserSubscriptionMap.user_email == user_email).filter(UserSubscriptionMap.subscription_name == subscription_name).first()


def create_user_subscription_map(db: Session, user_subscription_map: UserSubscriptionMapSchema):
    new_user_subscription_map = UserSubscriptionMap(
        subscription_name=user_subscription_map.subscription_name,
        user_email=user_subscription_map.user_email,
        card_owner_id=user_subscription_map.card_owner_id,
        card_number=user_subscription_map.card_number,
        cvv=user_subscription_map.cvv,
        start_date=user_subscription_map.start_date,
        expiration_date=user_subscription_map.expiration_date,
    )
    db.add(new_user_subscription_map)
    db.commit()
    db.refresh(new_user_subscription_map)
    return new_user_subscription_map


def delete_user_subscription_map_by_user_email_subscription_name(db: Session, user_email: str, subscription_name: str):
    user_subscription_map = get_user_subscription_map_by_user_email_subscription_name(
        db=db, user_email=user_email, subscription_name=subscription_name
    )

    db.delete(user_subscription_map)
    db.commit()


def update_user_subscription_map_by_user_email_subscription_name(db: Session, user_email: str, subscription_name: str, user_subscription_map: UserSubscriptionMapSchema):
    old_user_subscription_map = get_user_subscription_map_by_user_email_subscription_name(
        db=db, user_email=user_email, subscription_name=subscription_name
    )

    old_user_subscription_map.card_owner_id = user_subscription_map.card_owner_id if user_subscription_map.card_owner_id else old_user_subscription_map.card_owner_id
    old_user_subscription_map.card_number = user_subscription_map.card_number if user_subscription_map.card_number else old_user_subscription_map.card_number
    old_user_subscription_map.cvv = user_subscription_map.cvv if user_subscription_map.cvv else old_user_subscription_map.cvv

    db.commit()
    db.refresh(old_user_subscription_map)
    return old_user_subscription_map
