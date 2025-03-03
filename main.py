from typing import List

from fastapi import FastAPI, File, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

IMAGEDIR = 'images/'

app = FastAPI()
app.mount('/images', StaticFiles(directory='images'), name='images')
templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post('/upload-files')
async def upload_files(request: Request, files: List[UploadFile] = File(...)):
    for file in files:
        contents = await file.read()
        with open(f'{IMAGEDIR}{file.filename}', 'wb') as f:
            f.write(contents)

    show = [file.filename for file in files]

    # return {'Result': 'OK', 'filenames': [file.filename for file in files]}
    return templates.TemplateResponse(
        'index.html', {'request': request, 'show': show}
    )
