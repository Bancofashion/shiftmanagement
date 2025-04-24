from fastapi import FastAPI
from auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from users import router as users_router
from planning import router as planning_router
from facturatie import router as facturatie_router
from opdrachtgevers import router as opdrachtgevers_router
from export import router as export_router
from tijdlijn import router as tijdlijn_router
from favorieten import router as favorieten_router
from agenda import router as agenda_router
from auto_approval import router as auto_approval_router
from dienstaanvragen import router as dienstaanvragen_router
from factuursjablonen import router as factuursjablonen_router
from dashboard import router as dashboard_router
from tarieven import router as tarieven_router
from pdf_export import router as pdf_export_router
from verloning import router as verloning_router
from employee_profiles import employee_profiles_router, payroll_router
from medewerkers import router as medewerkers_router
from locations import router as locations_router
from database import engine
from models import Base
from init_db import init_db
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Medewerker Planning en Facturatie Systeem",
    description="API voor het beheren van planning, facturatie en verloning.",
    version="0.1.0"
)

# Configure CORS - MUST BE BEFORE ANY ROUTES
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://69.28.88.205"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=3600,  # Cache preflight requests for 1 hour
)

# Include routers
app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(users_router, prefix="/api", tags=["users"])
app.include_router(planning_router, prefix="/api", tags=["planning"])
app.include_router(facturatie_router, prefix="/api", tags=["facturatie"])
app.include_router(opdrachtgevers_router, prefix="/api", tags=["opdrachtgevers"])
app.include_router(export_router, prefix="/api", tags=["export"])
app.include_router(tijdlijn_router, prefix="/api", tags=["tijdlijn"])
app.include_router(favorieten_router, prefix="/api", tags=["favorieten"])
app.include_router(agenda_router, prefix="/api", tags=["agenda"])
app.include_router(auto_approval_router, prefix="/api", tags=["auto_approval"])
app.include_router(dienstaanvragen_router, prefix="/api", tags=["dienstaanvragen"])
app.include_router(factuursjablonen_router, prefix="/api", tags=["factuursjablonen"])
app.include_router(dashboard_router, prefix="/api", tags=["dashboard"])
app.include_router(tarieven_router, prefix="/api", tags=["tarieven"])
app.include_router(pdf_export_router, prefix="/api", tags=["pdf_export"])
app.include_router(verloning_router, prefix="/api", tags=["verloning"])
app.include_router(employee_profiles_router, prefix="/api", tags=["employee_profiles"])
app.include_router(payroll_router, prefix="/api", tags=["payroll"])
app.include_router(medewerkers_router, prefix="/api", tags=["medewerkers"])
app.include_router(locations_router, prefix="/api", tags=["locations"])

# Create database tables and initialize admin on startup
@app.on_event("startup")
async def startup_event():
    logger.info("Running database initialization...")
    init_db()
    logger.info("Database initialization completed!")

# Remove the middleware that's causing conflicts
# @app.middleware("http")
# async def add_cors_headers(request, call_next):
#     response = await call_next(request)
#     response.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"
#     response.headers["Access-Control-Allow-Credentials"] = "true"
#     response.headers["Access-Control-Allow-Methods"] = "*"
#     response.headers["Access-Control-Allow-Headers"] = "*"
#     return response

@app.get("/")
async def root():
    return {"message": "Welkom bij het Planning en Facturatie Systeem!"}

# ✅ Start de server correct
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
