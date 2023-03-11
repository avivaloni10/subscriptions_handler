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


@router.post("/")
async def create(request: RequestUserSubscriptionMap, db: Session = Depends(get_db)):
    user_subscription_map_crud.create_user_subscription_map(db, request.parameter)
    return Response(code=200, status="OK", message="UserSubscriptionMap created successfully").dict(exclude_none=True)


@router.get("/")
async def get(db: Session = Depends(get_db)):
    user_subscription_maps = user_subscription_map_crud.get_user_subscription_maps(db, 0, 100)

    return Response(
        code=200, status="OK", message="UserSubscriptionMaps batch fetched successfully", result=user_subscription_maps
    ).dict(exclude_none=True)


@router.get("/{user_email}/{subscription_name}")
async def get_by_user_email_subscription_name(user_email: str, subscription_name: str, db: Session = Depends(get_db)):
    user_subscription_map = user_subscription_map_crud.get_user_subscription_map_by_user_email_subscription_name(
        db, user_email, subscription_name
    )

    if not user_subscription_map:
        raise HTTPException(status_code=404, detail="UserSubscriptionMap not found")
    return Response(
        code=200, status="OK", message="UserSubscriptionMap fetched successfully", result=user_subscription_map
    ).dict(exclude_none=True)


@router.put("/{user_email}/{subscription_name}")
async def update_by_user_email_subscription_name(
        user_email: str, subscription_name: str, request: RequestUserSubscriptionMap, db: Session = Depends(get_db)
):
    user_subscription_map = user_subscription_map_crud.get_user_subscription_map_by_user_email_subscription_name(
        db, user_email, subscription_name
    )

    if not user_subscription_map:
        raise HTTPException(status_code=404, detail="UserSubscriptionMap not found")

    user_subscription_map = user_subscription_map_crud.update_user_subscription_map_by_user_email_subscription_name(
        db, user_email, subscription_name, request.parameter
    )

    return Response(
        code=200, status="OK", message="UserSubscriptionMap updated successfully", result=user_subscription_map
    ).dict(exclude_none=True)


@router.delete("/{user_email}/{subscription_name}")
async def delete_by_user_email_subscription_name(
        user_email: str, subscription_name: str, db: Session = Depends(get_db)
):
    user_subscription_map = user_subscription_map_crud.get_user_subscription_map_by_user_email_subscription_name(
        db, user_email, subscription_name
    )

    if not user_subscription_map:
        raise HTTPException(status_code=404, detail="UserSubscriptionMap not found")

    user_subscription_map_crud.delete_user_subscription_map_by_user_email_subscription_name(
        db, user_email, subscription_name
    )

    return Response(code=200, status="OK", message="UserSubscriptionMap deleted successfully").dict(exclude_none=True)
