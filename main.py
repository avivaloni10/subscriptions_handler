from fastapi import FastAPI

from routers import subscriptions_router
from routers import user_subscription_maps_router
from config.db import engine
from models import user
from models import subscription
from models import user_subscription_map

user.Base.metadata.create_all(bind=engine)
subscription.Base.metadata.create_all(bind=engine)
user_subscription_map.Base.metadata.create_all(bind=engine)

app = FastAPI()


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