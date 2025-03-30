from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User
from database import get_db

router = APIRouter()

@router.post("/transfer/")
def transfer_money(sender_id: int, receiver_id: int, amount: float, db: Session = Depends(get_db)):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")

    sender = db.query(User).filter(User.id == sender_id).first()
    receiver = db.query(User).filter(User.id == receiver_id).first()

    
    if not sender or not receiver:
        raise HTTPException(status_code=404, detail="Sender or receiver does not exist")

    if sender.balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient balance in sender's account")

    try:
        sender.balance -= amount
        receiver.balance += amount
        db.commit()
        return {"message": "Transfer successful", "sender_balance": sender.balance, "receiver_balance": receiver.balance}
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Transaction failed")
