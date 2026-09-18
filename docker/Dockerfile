FROM python:3.12-slim
WORKDIR /app

COPY . .

COPY pyproject.toml ./

RUN pip install .

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
