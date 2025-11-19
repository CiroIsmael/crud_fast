from fastapi import FastAPI
from apis import product_api, cliente_api, pedido_api
from database import engine
from repositories import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(product_api.router, prefix="/api", tags=["products"])
app.include_router(cliente_api.router, prefix="/api", tags=["clientes"])
app.include_router(pedido_api.router, prefix="/api", tags=["pedidos"])


@app.get("/")
def read_root():
    return {"Hello": "World"}
