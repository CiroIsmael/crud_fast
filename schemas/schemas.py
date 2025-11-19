from pydantic import BaseModel
from datetime import datetime

class ProductBase(BaseModel):
    nombre: str
    cantidad: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True

class ClienteBase(BaseModel):
    nombre: str
    email: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int

    class Config:
        from_attributes = True

class PedidoBase(BaseModel):
    cliente_id: int
    producto_id: int
    cantidad: int

class PedidoCreate(PedidoBase):
    pass

class Pedido(PedidoBase):
    id: int
    fecha: datetime

    class Config:
        from_attributes = True
