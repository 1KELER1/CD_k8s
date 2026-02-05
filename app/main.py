from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# Монтируем статические файлы
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get_home():
    return FileResponse("static/index.html")

@app.get("/api/hello")
async def hello():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
