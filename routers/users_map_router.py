from fastapi import APIRouter, Depends, HTTPException
from config.db import SessionLocal
from sqlalchemy.orm import Session
from schemas.user_subscription_map_schemas import RequestUserSubscriptionMap, Response
from dal import user_subscription_map as user_subscription_map_crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{user_email}")
async def get_by_user_email(user_email: str, db: Session = Depends(get_db)):
    user_subscription_maps = user_subscription_map_crud.get_user_subscriptions_by_user_email(db, user_email)

    if not user_subscription_maps:
        raise HTTPException(status_code=404, detail="No subscriptions for this user.")
    return Response(
        code=200, status="OK", message="UserSubscriptionMap fetched successfully", result=user_subscription_maps
    ).dict(exclude_none=True)
