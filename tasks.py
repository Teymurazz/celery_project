import requests
from celery_app import app
from sqlalchemy.orm import Session
from database import SessionLocal, APIData

API_URL = "https://api.api_url.com/data"

@app.task
def fetch_and_store_api_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()

        db = SessionLocal()
        api_data = APIData(data=str(data))
        db.add(api_data)
        db.commit()
        db.close()
