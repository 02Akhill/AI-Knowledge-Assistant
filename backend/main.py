from fastapi import FastAPI

from backend.routers.upload_router import router as upload_router


app = FastAPI(
    title="AI Knowledge Assistant",
    version="0.8"
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