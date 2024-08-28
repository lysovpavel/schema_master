FROM python:3.11.6-slim-bullseye

ENV DEBUG=False

WORKDIR /code

COPY poetry.lock pyproject.toml ./

RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y \
    gdal-bin libgdal-dev \
    python3-gdal \
    binutils libproj-dev

RUN python -m pip install --no-cache-dir poetry==1.4.2 \
    && poetry config virtualenvs.create false \
    && poetry install --without dev,test --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}

COPY ./src ./backend
COPY ./run.sh /code/
WORKDIR /code/backend

CMD ["/bin/bash", "/code/run.sh"]
