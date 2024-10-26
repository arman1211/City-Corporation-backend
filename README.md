# City Corporation Backend

This repository contains the backend for the City Corporation project, built with Django and Django Rest Framework. The project includes functionalities for citizens to report problems, request services, and communicate with authorities.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)

## Features

- User authentication with login and logout
- Citizens can report problems and request services
- Authorities can solve reported problems and service requests
- Real-time chat functionality between citizens and authorities
- Contact form for inquiries

## Requirements

- Python 3.x
- Django
- Django Rest Framework
- djangorestframework-simplejwt

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/city-corporation-backend.git
    cd city-corporation-backend
    ```

2. **Create and Activate a Virtual Environment**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Database**
    - Ensure you have a PostgreSQL database or any other supported database and update the `DATABASES` setting in your Django `settings.py` file.

5. **Run Migrations**
    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser**
    ```bash
    python manage.py createsuperuser
    ```

## Running the Server

Start the development server:

```bash
python manage.py runserver
```

## API Endpoints

### User Authentication
- **Login**  
  `POST /api/user/login/`  
  Authenticate a user and retrieve access tokens.

- **Logout**  
  `POST /api/user/logout/`  
  Invalidate the user session and log out.

### Citizen Management
- **Register Citizen**  
  `POST /api/citizen/register/`  
  Register a new citizen account.

- **List Citizens**  
  `GET /api/citizen/list/`  
  Retrieve a list of all citizens (authentication required).

- **Activate Citizen Account**  
  `GET /api/citizen/active/<uid64>/<token>/`  
  Activate a newly registered citizen account via token.

- **Update Citizen Profile**  
  `PATCH /api/citizen/update/<int:id>/`  
  Update the citizen's profile information.

- **Change Citizen Password**  
  `PATCH /api/citizen/update-password/<int:id>/`  
  Change the citizen's password.

### Authority Management
- **Register Authority**  
  `POST /api/authority/register/`  
  Register a new authority account.

- **List Authorities**  
  `GET /api/authority/list/`  
  Retrieve a list of all authorities (authentication required).

- **Activate Authority Account**  
  `GET /api/authority/active/<uid64>/<token>/`  
  Activate a newly registered authority account via token.

- **Update Authority Profile**  
  `PATCH /api/authority/update/<int:id>/`  
  Update the authority's profile information.

### Problem Reporting
- **Report Problem**  
  `POST /api/services/report-problem/`  
  Report a new problem by a citizen.

- **List Reported Problems**  
  `GET /api/services/problem/list/`  
  Retrieve a list of all reported problems (authentication required).

- **Get Problem Details**  
  `GET /api/services/problem/<int:problem_id>/`  
  Get details of a specific reported problem.

- **Solve Problem**  
  `PATCH /api/services/problem/solve/<int:problem_id>/`  
  Update the status of a reported problem to solved.

### Service Requests
- **Request Service**  
  `POST /api/services/request/`  
  Request a new service by a citizen.

- **List Service Requests**  
  `GET /api/services/request/list/`  
  Retrieve a list of all service requests (authentication required).

- **Get Service Request Details**  
  `GET /api/services/request/<int:request_id>/`  
  Get details of a specific service request.

- **Solve Service Request**  
  `PATCH /api/services/request/solve/<int:request_id>/`  
  Update the status of a service request to solved.

### Chat Functionality
- **Create Chat Room**  
  `POST /api/chat/room/`  
  Create a new chat room for citizen-authority communication.

- **Send Message**  
  `POST /api/chat/message/send/`  
  Send a message within a chat room.

- **Get Chat Room Messages**  
  `GET /api/chat/room/<int:room_id>/messages/`  
  Retrieve messages from a specific chat room.

- **List All Chat Rooms**  
  `GET /api/chat/room/list/`  
  Retrieve a list of all chat rooms.

### Contact Management
- **Post Contact Message**  
  `POST /api/contact/post/`  
  Submit a new contact inquiry.

- **Get Contact Messages**  
  `GET /api/contact/get/`  
  Retrieve all contact inquiries.
