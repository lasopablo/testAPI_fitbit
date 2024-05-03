from datetime import date

from fastapi import APIRouter

from tryvital.models import Activity, Credentials

router = APIRouter()


from fastapi import Query, HTTPException
from pydantic import BaseModel
import uuid 
from typing import List

class Activity(BaseModel):
    id: uuid.UUID
    user_id: str
    date: date
    steps: int
    calories: int

# Assuming a dictionary to mock database interactions
activities_db = {}


@router.get("/activity", response_model=List[Activity])
async def get_activity(
    start_date: date = Query(...),
    end_date: date = Query(...),
    vital_user_id: str = Query(...)
) -> List[Activity]:
    """
    Get stored activity data of a user.
    """
    print("hit")
    if start_date > end_date:
        raise HTTPException(status_code=400, detail="Start date must be before end date.")

    if vital_user_id in activities_db:
        activities = activities_db[vital_user_id]
        # Filter activities based on date range
        filtered_activities = [
            activity for activity in activities
            if start_date <= activity.date <= end_date
        ]
        print(filtered_activities)
        return filtered_activities

    return []  # Return an empty list if no activities or no user found


from datetime import datetime, timedelta

from fastapi import APIRouter, HTTPException, Header
from datetime import datetime, timedelta
import requests


@router.post("/fitbit/connect/{vital_user_id}")
async def connect_fitbit(vital_user_id: str) -> str:
    """
    Callback when a user has successfully authenticated with Fitbit.
    """
    # Assuming the token is provided by the interviewer in the Credentials class
    credentials = Credentials(access_token="sk_us_ZmKVnviws-2G7tw4NdcpiqMUcaUGrXiycJeneh0iX68")

    end_date = datetime.now()
    data = []
    for i in range(7):  # Fetch data for the last 7 days
        date = (end_date - timedelta(days=i)).strftime('%Y-%m-%d')
        url = f"https://api.fitbit.com/1/user/{vital_user_id}/activities/date/{date}.json"
        headers = {'Authorization': f"Bearer {credentials.access_token}"}
        response = requests.get(url, headers=headers)
        print(response)
        if response.status_code == 200:
            data.append(response.json())
        else:
            # This will log the error details and stop the loop if an API call fails
            error_detail = response.json() if response.text else response.reason
            print(error_detail)
            # Mock data setup
            print("mocking data...") # to pratice while i do not have the token with access
            current_date = datetime.now()
            activities_db[vital_user_id] = [
                Activity(
                    id=uuid.uuid4(),
                    user_id=vital_user_id,
                    date=current_date.date() - timedelta(days=i),
                    steps=1000 * i,
                    calories=300 * i
                ) for i in range(7)
            ]
            print(activities_db)
            raise HTTPException(status_code=response.status_code, detail=f"Error fetching data from Fitbit API: {error_detail}")

    return {"status": "success", "data": data}

