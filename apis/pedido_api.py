from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import pedido_service
from schemas import schemas
from database import get_db
from typing import List

router = APIRouter()

@router.post("/pedidos/", response_model=schemas.Pedido)
def create_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(get_db)):
    return pedido_service.create_pedido(db=db, pedido=pedido)

@router.get("/pedidos/", response_model=List[schemas.Pedido])
def read_pedidos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pedidos = pedido_service.get_pedidos(db, skip=skip, limit=limit)
    return pedidos

@router.get("/pedidos/{pedido_id}", response_model=schemas.Pedido)
def read_pedido(pedido_id: int, db: Session = Depends(get_db)):
    db_pedido = pedido_service.get_pedido(db, pedido_id=pedido_id)
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido not found")
    return db_pedido

@router.put("/pedidos/{pedido_id}", response_model=schemas.Pedido)
def update_pedido(pedido_id: int, pedido: schemas.PedidoCreate, db: Session = Depends(get_db)):
    db_pedido = pedido_service.update_pedido(db, pedido_id, pedido)
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido not found")
    return db_pedido

@router.delete("/pedidos/{pedido_id}", response_model=schemas.Pedido)
def delete_pedido(pedido_id: int, db: Session = Depends(get_db)):
    db_pedido = pedido_service.delete_pedido(db, pedido_id)
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido not found")
    return db_pedido
