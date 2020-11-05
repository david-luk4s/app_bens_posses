# Imagem Python
FROM python:3.8

# setando diretorio de trabalho
WORKDIR /code/app_desafio_inquest

# Nao gravar .pyc arquivos
ENV PYTHONDONTWRITEBYTECODE 1

# Atualizar pip
RUN pip install --upgrade pip

# Copiar requirements da app
COPY ./requirements.txt /code/app_desafio_inquest/requirements.txt

# Instalar todas dependencias
RUN pip install -r requirements.txt

# Copiar app para diretorio de trabalho
COPY . /code/app_desafio_inquest/