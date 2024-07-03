FROM python:3.9.19-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .
RUN apt-get update
RUN apt-get install -y build-essential python3-greenlet pip git wget
RUN pip install "poetry"
RUN poetry config virtualenvs.create false
RUN poetry lock --no-update
RUN poetry install --no-dev
# ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app.server:app"]
ENTRYPOINT ["python3","main.py"]
