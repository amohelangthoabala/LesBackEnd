from fastapi import FastAPI
from interface.routes import users, authentication
from infrastructure.orm.sqlalchemy import models
from infrastructure.database.database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)
#models.Base.metadata.drop_all(engine)

app.include_router(authentication.router)
app.include_router(users.router)
