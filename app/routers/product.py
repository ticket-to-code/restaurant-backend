from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_active_owner
from app.models.user import User
from app.schemas.product import ProductListResponse, PaginatedProducts
from app.services import product as product_service

router = APIRouter()


@router.get("/products", response_model=PaginatedProducts)
async def get_products(
    category_id: int | None = Query(None),
    search: str | None = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    current_user: User = Depends(get_current_active_owner),
    db: AsyncSession = Depends(get_db)
):
    """Get products with optional filtering by category and search (Owner only)"""
    products, total_count = await product_service.list_products_with_count(
        db, current_user.restaurant_id, category_id, search, skip, limit
    )

    # Enrich with category names
    from app.models.category import Category

    enriched: list[ProductListResponse] = []
    for product in products:
        cat_result = await db.execute(
            select(Category).where(Category.id == product.category_id)
        )
        category = cat_result.scalars().first()
        enriched.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "category_id": product.category_id,
            "category_name": category.name if category else "",
            "is_available": product.is_available,
            "image_url": product.image_url,
            "created_at": product.created_at
        })

    return {
        "items": enriched,
        "total_count": total_count,
        "skip": skip,
        "limit": limit,
    }
