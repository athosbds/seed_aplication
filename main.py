from fastapi import FastAPI
from views.view import router as api_router

app = FastAPI(title='BNPL_API - Prontu')

app.include_router(api_router, prefix="/api")

# Rota Raiz para validar API
@app.get("/")
def read_root():
    return {"message": "BNPL_API is running!"}