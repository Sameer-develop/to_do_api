from fastapi import FastAPI
from app.routes import person_routes

app = FastAPI(title="Development Branch API")

# Register routes
app.include_router(person_routes.router, prefix="/persons", tags=["Persons"])

@app.get("/")
def home():
    return {"message": "Welcome to the Development Branch API"}
