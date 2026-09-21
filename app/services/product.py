from typing import List, Optional, Tuple

from sqlalchemy import select, and_, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product


async def count_products_in_category(db: AsyncSession, category_id: int) -> int:
    """Count active products in a category"""
    result = await db.execute(
        select(func.count()).select_from(Product).where(
            and_(
                Product.category_id == category_id,
                Product.deleted_at.is_(None)
            )
        )
    )
    return result.scalar() or 0


async def list_products_with_count(
    db: AsyncSession,
    restaurant_id: int,
    category_id: Optional[int],
    search: Optional[str],
    skip: int,
    limit: int,
) -> Tuple[List[Product], int]:
    conditions = [
        Product.restaurant_id == restaurant_id,
        Product.deleted_at.is_(None),
    ]

    if category_id is not None:
        conditions.append(Product.category_id == category_id)

    if search:
        # Case-insensitive match on name
        conditions.append(Product.name.ilike(f"%{search}%"))

    count_result = await db.execute(
        select(func.count()).select_from(Product).where(and_(*conditions))
    )
    total_count = count_result.scalar() or 0

    query = (
        select(Product)
        .where(and_(*conditions))
        .order_by(Product.created_at.desc())
        .offset(skip)
        .limit(limit)
    )

    items_result = await db.execute(query)
    items = items_result.scalars().all()

    return items, total_count
