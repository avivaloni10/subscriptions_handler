from fastapi import FastAPI, Depends
from sqlalchemy.exc import IntegrityError

from routers import subscriptions_router
from routers import user_subscription_maps_router
from routers import users_map_router
from config.db import engine, SessionLocal
from models import user
from models import subscription
from models import user_subscription_map

from dal import subscription as subscription_crud
from schemas.subscription_schemas import SubscriptionSchema

user.Base.metadata.create_all(bind=engine)
subscription.Base.metadata.create_all(bind=engine)
user_subscription_map.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ping")
async def ping():
    return {"pong"}


app.include_router(
    subscriptions_router.router, prefix="/subscriptions", tags=["subscriptions"]
)

app.include_router(
    user_subscription_maps_router.router, prefix="/user_subscription_maps", tags=["user_subscription_maps"]
)

app.include_router(
    users_map_router.router, prefix="/users_map", tags=["users_map"]
)


def create_subscription(name: str, description: str) -> None:
    print(f"Creating {name} subscriptions")
    try:
        db = SessionLocal()
        subscription_crud.create_subscription(db, SubscriptionSchema(name=name, description=description))
        db.close()
    except IntegrityError as ie:
        print(f"{name} subscription already exists")


create_subscription("Basic", "Basic subscription")
create_subscription("Premium", "Premium subscription")
