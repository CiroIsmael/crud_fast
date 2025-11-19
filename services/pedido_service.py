from sqlalchemy.orm import Session
from repositories import pedido_repository
from schemas import schemas

def get_pedido(db: Session, pedido_id: int):
    return pedido_repository.get_pedido(db, pedido_id)

def get_pedidos(db: Session, skip: int = 0, limit: int = 100):
    return pedido_repository.get_pedidos(db, skip=skip, limit=limit)

def create_pedido(db: Session, pedido: schemas.PedidoCreate):
    return pedido_repository.create_pedido(db, pedido)

def update_pedido(db: Session, pedido_id: int, pedido: schemas.PedidoCreate):
    return pedido_repository.update_pedido(db, pedido_id, pedido)

def delete_pedido(db: Session, pedido_id: int):
    return pedido_repository.delete_pedido(db, pedido_id)
