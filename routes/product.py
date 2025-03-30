from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Product
from schemas import ProductCreate

router = APIRouter()

@router.post("/products/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    if product.stock < 0:
        raise HTTPException(status_code=400, detail="Stock cannot be negative")
    
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"message": "Product registered successfully", "product": new_product}
