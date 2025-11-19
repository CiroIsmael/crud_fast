from sqlalchemy.orm import Session
from repositories import product_repository
from schemas import schemas

def get_product(db: Session, product_id: int):
    return product_repository.get_product(db, product_id)

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return product_repository.get_products(db, skip=skip, limit=limit)

def create_product(db: Session, product: schemas.ProductCreate):
    return product_repository.create_product(db, product)

def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    return product_repository.update_product(db, product_id, product)

def delete_product(db: Session, product_id: int):
    return product_repository.delete_product(db, product_id)