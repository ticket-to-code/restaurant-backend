from typing import Optional
from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.product import (
    ProductCreate,
    ProductRead,
    ProductUpdate,
    ProductListResponse,
)
from app.services import product as product_service

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=ProductListResponse)
async def list_products(
    restaurant_id: int,
    category_id: Optional[int] = None,
    search: Optional[str] = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: AsyncSession = Depends(get_db),
):
    """Return a paginated list of products with total count and filter metadata."""
    return await product_service.get_products(
        db=db,
        restaurant_id=restaurant_id,
        category_id=category_id,
        search=search,
        skip=skip,
        limit=limit,
    )


@router.get("/{product_id}", response_model=ProductRead)
async def get_product(
    product_id: int,
    restaurant_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Return a single product by ID."""
    product = await product_service.get_product(
        db=db, product_id=product_id, restaurant_id=restaurant_id
    )
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return product


@router.post("/", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_in: ProductCreate,
    db: AsyncSession = Depends(get_db),
):
    """Create a new product."""
    return await product_service.create_product(db=db, product_data=product_in.model_dump())


@router.patch("/{product_id}", response_model=ProductRead)
async def update_product(
    product_id: int,
    restaurant_id: int,
    product_in: ProductUpdate,
    db: AsyncSession = Depends(get_db),
):
    """Update an existing product."""
    product = await product_service.update_product(
        db=db,
        product_id=product_id,
        restaurant_id=restaurant_id,
        update_data=product_in.model_dump(exclude_unset=True),
    )
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: int,
    restaurant_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Soft-delete a product."""
    product = await product_service.delete_product(
        db=db, product_id=product_id, restaurant_id=restaurant_id
    )
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
