from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.auth.routes import router as auth_router
from app.core.config import settings
from app.api.v1.users.routes import router as user_router
from app.api.v1.organizations.routes import router as organization_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(organization_router)



@app.get("/")
def root():
    return {
        "message": "AI Recruitment Platform API",
        "version": settings.APP_VERSION,
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": settings.APP_NAME,
    }