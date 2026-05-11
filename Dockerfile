FROM python:3.12-slim

WORKDIR /fraud-detection-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ("uvicorn", "backend_app:app", "--reload")