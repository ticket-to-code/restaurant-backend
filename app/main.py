from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import engine, Base
from app.routers import auth, category, product, order, sales, pos, settings, dashboard
# Import models to ensure they are registered with Base.metadata
from app.models import User, Restaurant, Branch, Category, Product, Order, OrderItem, RestaurantSettings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup as per CLAUDE.md requirement
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="Restaurant Management System API",
    description="SaaS Restaurant Management System MVP API",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(auth.router)
app.include_router(category.router)
app.include_router(product.router)
app.include_router(order.router)
app.include_router(sales.router)
app.include_router(pos.router)
app.include_router(settings.router)
app.include_router(dashboard.router)

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok", "message": "Restaurant Backend is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
