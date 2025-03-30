from pydantic import BaseModel, Field

# Pydantic model for user creation
class UserCreate(BaseModel):
    name: str
    password: str
    balance: float = Field(gt=0, description="Balance must be positive")


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float = Field(gt=0, description="Price must be positive")
    stock: int

    @classmethod
    def validate_stock(cls, value):
        if value < 0:
            raise ValueError("Stock cannot be negative")
        return value
