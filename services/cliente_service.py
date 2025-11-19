from sqlalchemy.orm import Session
from repositories import cliente_repository
from schemas import schemas

def get_cliente(db: Session, cliente_id: int):
    return cliente_repository.get_cliente(db, cliente_id)

def get_clientes(db: Session, skip: int = 0, limit: int = 100):
    return cliente_repository.get_clientes(db, skip=skip, limit=limit)

def get_cliente_by_email(db: Session, email: str):
    return cliente_repository.get_cliente_by_email(db, email)

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    return cliente_repository.create_cliente(db, cliente)

def update_cliente(db: Session, cliente_id: int, cliente: schemas.ClienteCreate):
    return cliente_repository.update_cliente(db, cliente_id, cliente)

def delete_cliente(db: Session, cliente_id: int):
    return cliente_repository.delete_cliente(db, cliente_id)
