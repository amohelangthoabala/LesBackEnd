from fastapi import FastAPI
from routers import users, authentication
import models
from config.database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)
#models.Base.metadata.drop_all(engine)

app.include_router(authentication.router)
app.include_router(users.router)
