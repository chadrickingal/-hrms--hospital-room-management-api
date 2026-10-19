from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.database import engine
from app.core.base import Base

from app.api.routers import router


@asynccontextmanager
async def lifespan(app : FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(
    title="HBMS API", 
    lifespan=lifespan
)

# ===================================================
#   HEALTH CHECK   
# ===================================================
@app.get("/")
def health_check():
    return{
        "msg":"HBMS is running..."
    }

# ===================================================
#   Register Main Route  
# ===================================================

app.include_router(
    router,
    prefix="/api/v1"
)