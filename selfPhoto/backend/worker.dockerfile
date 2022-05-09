FROM python:3.10

RUN apt-get update && apt-get install -y libwebp-dev && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
RUN mkdir /assets

COPY /app /app
COPY app/pyproject.toml /app/app
COPY app/start_worker.sh /app

WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install



RUN chmod +x start_worker.sh

CMD ["bash", "start_worker.sh"]