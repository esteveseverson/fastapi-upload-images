# Upload de Imagens no FastAPI
## Visão Geral
- Este sistema foi feito para fins de estudo e tem como objetivo permitir que os usuários façam upload de arquivos de imagem e visualizem uma galeria com as imagens enviadas. <br>
- O projeto FastAPI + Jinja2 é uma aplicação web que permite o upload e visualização de imagens. A aplicação utiliza FastAPI como framework para criação da API e Jinja2 para renderização de templates HTML. <br>
- O gerenciamento de pacotes é feito com o Uvicorn, que é o servidor ASGI utilizado para rodar a aplicação.
---

## Tecnologias Utilizadas
- FastAPI: Framework web para construção da API.
- Jinja2: Motor de templates utilizados para renderizar páginas HTML.
- Uvicorn: Servidor ASGI utilizado para rodar a aplicação FastAPI
- Glob: Módulo usado para localizar arquivos com base em padrão de caminho.

---
## Estrutura do projeto
```
fastapi-upload-images/
├─ templates/                  # templates do Jinja2
│  ├─ all-images.html
│  ├─ base.html
│  ├─ index.html
├─ .gitignore
├─ .python-version
├─ main.py                     # arquivo principal
├─ pyproject.toml
├─ README.md
├─ uv.lock
```
## Instalação e Execução
1. Clone o repositório:
` git clone https://github.com/esteveseverson/fastapi-upload-images `
2. Acesse o repositório:
` cd fastapi-upload-images `
3. Instale as dependências utilizando o gerenciador de pacotes **uv**:
` uv install `
4. Inicie o servidor
` uv run main.py `

## Como utilizar a aplicação
A aplicação permite que o usuário faça o upload de arquivos de imagem e visualize todas as imagens enviadas na plataforma.
### Rota de Upload de Arquivos
POST `/upload-files`: Recebe um ou mais arquivos de imagem e os armazena no diretório images/.
- Parâmetros:
  - files: Lista de arquivos (UploadFile), onde o usuário deve selecionar um ou mais arquivos de imagem para o upload.
- Respostas:
  - 200 - OK: A página será retornada com uma mensagem de status
    - Status de sucesso: `Arquivos enviados`
    - Status de falha: `Falha ao enviar arquivos`

### Rota para Visualização das Imagens
GET `/all-images`: Exibe todas as imagens enviadas até o momento.
- Parâmetros: Nenhum
- Respostas:
  - 200 - OK: Retorna uma página com a lista de imagens enviadas, mostrando todas as imagens que foram armazenadas no diretório images/.

### Página Inicial
GET `/`: Exibe a página principal, onde o usuário pode fazer o upload de imagens.
- Parâmetros: Nenhum
- Respostas:
  - 200 - OK: A página inicial com o formulário de upload de arquivos é retornada.
