from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, or_, func
from fastapi import HTTPException, status
from datetime import datetime, timezone

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


async def _get_product_or_raise(
    db: AsyncSession,
    product_id: int,
    restaurant_id: int,
) -> Product:
    """
    Fetch an active product by id, then verify ownership.

    The existence check (404) is intentionally performed before the ownership
    check (403) so that callers always receive a meaningful "not found" error
    when the product simply does not exist, rather than a misleading
    "forbidden" that would reveal nothing about whether the resource exists.
    """
    result = await db.execute(
        select(Product).where(
            and_(Product.id == product_id, Product.deleted_at.is_(None))
        )
    )
    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    if product.restaurant_id != restaurant_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this product",
        )

    return product


async def get_products(
    db: AsyncSession,
    restaurant_id: int,
    category_id: int | None = None,
    search: str | None = None,
    skip: int = 0,
    limit: int = 100,
):
    """Get products with optional filtering by category and search"""
    conditions = [
        Product.restaurant_id == restaurant_id,
        Product.deleted_at.is_(None),
    ]

    if category_id:
        conditions.append(Product.category_id == category_id)

    if search:
        conditions.append(
            or_(
                func.lower(Product.name).contains(func.lower(search)),
                func.lower(Product.description).contains(func.lower(search)),
            )
        )

    query = (
        select(Product)
        .where(and_(*conditions))
        .order_by(Product.name)
        .offset(skip)
        .limit(limit)
    )
    result = await db.execute(query)
    return result.scalars().all()


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


async def create_product(
    db: AsyncSession,
    restaurant_id: int,
    product_data: ProductCreate,
):
    """Create a new product"""
    product = Product(
        restaurant_id=restaurant_id,
        name=product_data.name,
        description=product_data.description,
        price=product_data.price,
        category_id=product_data.category_id,
        image_url=product_data.image_url,
    )
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


async def update_product(
    db: AsyncSession,
    restaurant_id: int,
    product_id: int,
    product_data: ProductUpdate,
):
    """Update a product (owner must belong to the same restaurant)"""
    product = await _get_product_or_raise(db, product_id, restaurant_id)

    product.name = product_data.name
    product.price = product_data.price
    product.category_id = product_data.category_id
    product.description = product_data.description
    product.image_url = product_data.image_url

    await db.commit()
    await db.refresh(product)
    return product


async def toggle_product_availability(
    db: AsyncSession,
    restaurant_id: int,
    product_id: int,
):
    """Toggle the availability flag of a product"""
    product = await _get_product_or_raise(db, product_id, restaurant_id)

    product.is_available = not product.is_available

    await db.commit()
    await db.refresh(product)
    return product


async def delete_product(
    db: AsyncSession,
    restaurant_id: int,
    product_id: int,
):
    """Soft-delete a product by setting its deleted_at timestamp"""
    product = await _get_product_or_raise(db, product_id, restaurant_id)

    product.deleted_at = datetime.now(timezone.utc)

    await db.commit()
    await db.refresh(product)
    return product
