print("import dependencies...")
from fastapi import FastAPI
from interface.routes import users, authentication, message, chat
from infrastructure.orm.sqlalchemy import models
from infrastructure.database.database import engine

app = FastAPI()
print("app strating...")

models.Base.metadata.create_all(engine)
#models.Base.metadata.drop_all(engine)

@app.get('/')
def home():
    return "api running"

app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(chat.router)
app.include_router(message.router)

print("running...")
