from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

app = FastAPI()

templates = Environment(loader=FileSystemLoader('templates'))

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_index():
    template = templates.get_template('index.html')
    return HTMLResponse(content=template.render(), status_code=200)

# Другие импорты, модели и ендпоинты

# Пример ссылки на статику из шаблона
# <link rel="stylesheet" href="/static/styles.css">
