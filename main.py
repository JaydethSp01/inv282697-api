from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routers import producto, categoria, talla, proveedor, stock, usuario
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=os.environ.get("CORS_ORIGINS", "*").split(","), allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(producto.router)
app.include_router(categoria.router)
app.include_router(talla.router)
app.include_router(proveedor.router)
app.include_router(stock.router)
app.include_router(usuario.router)
@app.get("/health")
async def health():
    return {"status": "ok"}
