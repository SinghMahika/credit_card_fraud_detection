FROM python:3.12-slim

WORKDIR /credit_card_fraud_detection

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ("streamlit", "run", "app.py", "--server.address", "0.0.0.0")
