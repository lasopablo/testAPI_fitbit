from datetime import date

from fastapi import APIRouter

from tryvital.models import Activity, Credentials

import requests

from datetime import timedelta 
from datetime import datetime
import uuid

router = APIRouter()


@router.get("/activity")
async def get_activity(
    start_date: date,
    end_date: date,
    vital_user_id: str,
) -> list[Activity]:
    """
    Get stored activity data of a user.
    """
    activities = activities_db[vital_user_id]

    filtered_activities = [
        activity
        for activity in activities
        if start_date <= activity.date <= end_date
    ]
    print(filtered_activities)

    return filtered_activities

activities_db = {}

@router.post("/fitbit/connect/{vital_user_id}")
async def connect_fitbit(vital_user_id: str) -> str:
    """
    Callback when a user has successfully authenticated with Fitbit.
    """

    credentials = Credentials(access_token="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkM1NjMiLCJzdWIiOiI3M1Y2SzMiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd3BybyB3bnV0IHdzbGUgd3dlaSB3c29jIHdzZXQgd2FjdCB3bG9jIiwiZXhwIjoxNzE0NzU4MDYzLCJpYXQiOjE3MTQ3MjkyNjN9.lTZOwxJIx7tT-6GMf4D1PKM9e51a-Rcd5mVuCghy4XU")
    end_date = datetime.now()

    for i in range(7):
        date = (end_date - timedelta(days=i)).strftime("%Y-%m-%d")

        url = f"https://api.fitbit.com/1/user/-/activities/date/{date}.json"
        header = {'Authorization': f"Bearer {credentials.access_token}"}
        response = requests.get(url, headers=header)
        response_json = (response.json())
        calories = response_json['summary']['caloriesOut']
        steps = response_json['summary']['steps']

        if vital_user_id not in activities_db:
            activities_db[vital_user_id] = []

        activities_db[vital_user_id].append(Activity(
            id=uuid.uuid4(),
            user_id=vital_user_id,
            date=date,
            steps=steps,
            calories=calories,
        ))
        
        print(activities_db)


    print(f"Vital User ID: {vital_user_id}")

    return "Success"
