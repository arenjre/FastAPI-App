from fastapi import FastAPI
from database import engine, Base
from routes import auth, product, transactions

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(product.router)
app.include_router(transactions.router)
