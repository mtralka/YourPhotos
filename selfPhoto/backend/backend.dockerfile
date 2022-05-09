FROM python:3.10

RUN apt-get update && apt-get install -y libwebp-dev && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
RUN mkdir /assets

COPY /app /app
COPY app/pyproject.toml /app/app

WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
