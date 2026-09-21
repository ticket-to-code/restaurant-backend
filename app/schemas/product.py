from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: float
    category_id: Optional[int] = None
    image_url: Optional[str] = None


class ProductResponse(ProductBase):
    id: int
    is_available: bool
    created_at: datetime

    class Config:
        from_attributes = True


class ProductListResponse(ProductResponse):
    category_name: str = ""


class PaginatedProducts(BaseModel):
    items: List[ProductListResponse]
    total_count: int
    skip: int
    limit: int
