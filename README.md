# Fitbit Activity Tracker API

This project demonstrates a robust implementation of a RESTful API using FastAPI to interact with the Fitbit API for fetching and storing user activity data. This project is designed to showcase back-end skills in building scalable, maintainable APIs with Python.

![Screenshot_GUI](/Screenshot_GUI.png)


## Project Features

- **Fitbit API Integration**: Connects with Fitbit to retrieve 7 days of historical activity data.
- **Efficient Data Handling**: Implements endpoints to fetch and store data efficiently in a scalable manner.
- **Interactive API Documentation**: Utilizes FastAPI's automatic Swagger UI and Redoc to provide clear and interactive API documentation.

## Technologies Used

- FastAPI
- Python 3.10 - 3.12
- Poetry for dependency management

## Getting Started

### Prerequisites

Before installation, ensure you have Python 3.10-3.12 and Poetry installed on your system.

### Installation

Set up a virtual environment and install dependencies using Poetry:

```bash
poetry shell
poetry install
```


### Running the API

```bash
poetry run server
```

Expected standout output:
```bash
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [69443] using WatchFiles
INFO:     Started server process [69448]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```


### API Documentation

Explore the API:
- **Swagger UI**: Interactive API playground at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc**: Enhanced API documentation at [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Project Structure

```
tryvital
├── api
│   └── api_v1
│       ├── endpoints
│       │   └── api.py  # Endpoints are defined here.
│       └── router.py
|── models.py           # Pre-defined Pydantic models
└── main.py
```


## Key parts

1. **Callback Endpoint**:
   - `POST /v1/fitbit/connect/{vital_user_id}`
   - Fetches and stores 7 days of historical activity data from Fitbit.

2. **Query Endpoint**:
   - `GET /v1/activity`
   - Queries stored activity data based on user-specified date ranges.

## Further Information

- This project does not involve the actual OAuth flow with Fitbit.
- Refer to [Fitbit's Activity Summary API](https://dev.fitbit.com/build/reference/web-api/activity/get-daily-activity-summary/) for more details.

![Flow Diagram](/flow-diagram.png)
