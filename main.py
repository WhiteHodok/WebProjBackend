from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, Response
import os


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Делаем редирект на статику
@app.get("/", include_in_schema=False)
async def redirect_to_index():
    return Response(status_code=302, headers={"Location": "/static/index.html"})

# Немного обработчиков
@app.get("/style.css")
async def get_style():
    if not os.path.exists("static/css/style.css"):
        raise HTTPException(status_code=404)

    return FileResponse(path="static/css/style.css")


@app.get("/404.css")
async def get_404_style():
    if not os.path.exists("static/css/404.css"):
        raise HTTPException(status_code=404)

    return FileResponse(path="static/css/404.css")


@app.exception_handler(HTTPException)
async def handle_http_exception(error: HTTPException):
    if error.status_code == 404:
        return FileResponse(path="static/404.html")
    elif error.status_code == 500:
        return FileResponse(path="static/404.html")
    else:
        return error


