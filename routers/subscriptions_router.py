from fastapi import APIRouter, Depends, HTTPException
from config.db import SessionLocal
from sqlalchemy.orm import Session
from schemas.subscription_schemas import RequestSubscription, Response
from dal import subscription as subscription_crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
async def create(request: RequestSubscription, db: Session = Depends(get_db)):
    subscription_crud.create_subscription(db, request.parameter)
    return Response(code=200, status="OK", message="Subscription created successfully").dict(exclude_none=True)


@router.get("/")
async def get(db: Session = Depends(get_db)):
    subscriptions = subscription_crud.get_subscriptions(db, 0, 100)
    return Response(code=200, status="OK", message="Subscriptions batch fetched successfully", result=subscriptions).dict(
        exclude_none=True)


@router.get("/{name}")
async def get_by_name(name: str, db: Session = Depends(get_db)):
    subscription = subscription_crud.get_subscription_by_name(db, name)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return Response(code=200, status="OK", message="Subscription fetched successfully", result=subscription).dict(exclude_none=True)


@router.put("/{name}")
async def update_by_name(name: str, request: RequestSubscription, db: Session = Depends(get_db)):
    subscription = subscription_crud.get_subscription_by_name(db, name)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    subscription = subscription_crud.update_subscription_by_name(db, name, request.parameter)
    return Response(code=200, status="OK", message="Subscription updated successfully", result=subscription).dict(exclude_none=True)


@router.delete("/{name}")
async def delete_by_name(name: str, db: Session = Depends(get_db)):
    subscription = subscription_crud.get_subscription_by_name(db, name)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    subscription_crud.delete_subscription_by_name(db, name)
    return Response(code=200, status="OK", message="Subscription deleted successfully").dict(exclude_none=True)
