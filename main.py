from fastapi import FastAPI

app = FastAPI(title='BNPL_TEST')

@app.get('/offers')
def offers():
    return {
        "mensagem": "Olá"
    }