from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, or_, func
from app.models.product import Product


async def get_products(
    db: AsyncSession,
    restaurant_id: int,
    category_id: int | None = None,
    search: str | None = None,
    skip: int = 0,
    limit: int = 100,
):
    """Get products with optional filtering by category and search"""
    base_conditions = [
        Product.restaurant_id == restaurant_id,
        Product.deleted_at.is_(None),
    ]

    if category_id:
        base_conditions.append(Product.category_id == category_id)

    if search:
        base_conditions.append(
            or_(
                func.lower(Product.name).contains(func.lower(search)),
                func.lower(Product.description).contains(func.lower(search)),
            )
        )

    count_query = select(func.count(Product.id)).where(and_(*base_conditions))
    count_result = await db.execute(count_query)
    total = count_result.scalar() or 0

    query = (
        select(Product)
        .where(and_(*base_conditions))
        .order_by(Product.name)
        .offset(skip)
        .limit(limit)
    )
    result = await db.execute(query)
    items = result.scalars().all()

    return {
        "items": items,
        "total": total,
        "skip": skip,
        "limit": limit,
    }


async def get_product(db: AsyncSession, product_id: int, restaurant_id: int):
    """Get a single product by ID within a restaurant"""
    result = await db.execute(
        select(Product).where(
            and_(
                Product.id == product_id,
                Product.restaurant_id == restaurant_id,
                Product.deleted_at.is_(None),
            )
        )
    )
    return result.scalar_one_or_none()


async def get_products_by_category(
    db: AsyncSession, restaurant_id: int, category_id: int
):
    """Get all products in a specific category"""
    result = await db.execute(
        select(Product)
        .where(
            and_(
                Product.restaurant_id == restaurant_id,
                Product.category_id == category_id,
                Product.deleted_at.is_(None),
            )
        )
        .order_by(Product.name)
    )
    return result.scalars().all()


async def create_product(db: AsyncSession, product_data: dict):
    """Create a new product"""
    product = Product(**product_data)
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


async def update_product(
    db: AsyncSession, product_id: int, restaurant_id: int, update_data: dict
):
    """Update an existing product"""
    product = await get_product(db, product_id, restaurant_id)
    if not product:
        return None
    for field, value in update_data.items():
        if value is not None:
            setattr(product, field, value)
    await db.commit()
    await db.refresh(product)
    return product


async def delete_product(db: AsyncSession, product_id: int, restaurant_id: int):
    """Soft-delete a product"""
    from datetime import datetime

    product = await get_product(db, product_id, restaurant_id)
    if not product:
        return None
    product.deleted_at = datetime.utcnow()
    await db.commit()
    return product
