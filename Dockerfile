FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY src src

EXPOSE 8000

CMD ["uvicorn", "--factory", "src.main:create_app", "--host", "0.0.0.0"]