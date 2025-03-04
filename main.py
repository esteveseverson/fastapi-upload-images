from glob import glob
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


@app.post('/upload-files', response_class=HTMLResponse)
async def upload_files(request: Request, files: List[UploadFile] = File(...)):
    status = 'Falha ao enviar arquivos'

    try:
        for file in files:
            contents = await file.read()

            with open(f'{IMAGEDIR}{file.filename}', 'wb') as f:
                f.write(contents)

        status = 'Arquivos enviados'
        return templates.TemplateResponse(
            'index.html', {'request': request, 'status': status}
        )

    except Exception:
        return templates.TemplateResponse(
            'index.html', {'request': request, 'status': status}
        )


@app.get('/all-images', response_class=HTMLResponse)
def get_images(request: Request):
    all_images_dir = glob(IMAGEDIR + '*')
    all_images = []
    for image in all_images_dir:
        imagedir = image.replace(IMAGEDIR, '')
        all_images.append(imagedir)

    return templates.TemplateResponse(
        'all-images.html', {'request': request, 'all_images': all_images}
    )
