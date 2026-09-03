from typing import List, Optional
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    category_id: Optional[int] = None
    is_available: bool = True


class ProductCreate(ProductBase):
    restaurant_id: int


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    category_id: Optional[int] = None
    is_available: Optional[bool] = None


class ProductRead(ProductBase):
    id: int
    restaurant_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    items: List[ProductRead]
    total: int
    skip: int
    limit: int
