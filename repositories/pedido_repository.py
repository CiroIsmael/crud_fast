from sqlalchemy.orm import Session
from . import models
from schemas import schemas

def get_pedido(db: Session, pedido_id: int):
    return db.query(models.Pedido).filter(models.Pedido.id == pedido_id).first()

def get_pedidos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pedido).offset(skip).limit(limit).all()

def create_pedido(db: Session, pedido: schemas.PedidoCreate):
    db_pedido = models.Pedido(
        cliente_id=pedido.cliente_id,
        producto_id=pedido.producto_id,
        cantidad=pedido.cantidad
    )
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

def update_pedido(db: Session, pedido_id: int, pedido: schemas.PedidoCreate):
    db_pedido = db.query(models.Pedido).filter(models.Pedido.id == pedido_id).first()
    if db_pedido:
        db_pedido.cliente_id = pedido.cliente_id
        db_pedido.producto_id = pedido.producto_id
        db_pedido.cantidad = pedido.cantidad
        db.commit()
        db.refresh(db_pedido)
    return db_pedido

def delete_pedido(db: Session, pedido_id: int):
    db_pedido = db.query(models.Pedido).filter(models.Pedido.id == pedido_id).first()
    if db_pedido:
        db.delete(db_pedido)
        db.commit()
    return db_pedido
