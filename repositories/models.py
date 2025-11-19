from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database import Base
import datetime

class Product(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), index=True)
    cantidad = Column(Integer)

class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), index=True)
    email = Column(String(50), unique=True, index=True)

class Pedido(Base):
    __tablename__ = "pedido"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("cliente.id"))
    producto_id = Column(Integer, ForeignKey("producto.id"))
    cantidad = Column(Integer)
    fecha = Column(DateTime, default=datetime.datetime.utcnow)