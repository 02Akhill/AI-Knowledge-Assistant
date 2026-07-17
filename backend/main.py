from fastapi import FastAPI

from backend.routers.upload_router import router as upload_router
from backend.routers.chat_router import router as chat_router


app = FastAPI(
    title="AI Knowledge Assistant",
    version="0.9"
)


# ==========================================
# Home Endpoint
# ==========================================

@app.get("/")
def home():
    return {
        "message": "AI Knowledge Assistant is running."
    }


# ==========================================
# Routers
# ==========================================

app.include_router(upload_router)
app.include_router(chat_router)