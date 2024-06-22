# FlaskUserCountAPI

## Overview
FlaskUserCountAPI is a simple Flask application designed to track the number of users visiting a specific endpoint. The application utilizes a MongoDB database to persist the count of user visits.

## Application Structure


FlaskUserCountAPI
│
├── db
│ └── Dockerfile
├── env
├── web
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
├── docker-compose.yml
└── requirements.txt




## Features
- **User Visit Count:** Tracks how many times the `/hello` endpoint is visited and increments a count stored in MongoDB.
- **Restful API:** Utilizes Flask-RESTful for easy API management.

## Prerequisites
- Docker
- Docker Compose

## Setup and Installation
1. **Clone the repository:**
git clone https://github.com/yourusername/FlaskUserCountAPI.git
`cd FlaskUserCountAPI`


2. **Build and run the Docker containers:**
`docker-compose up --build
`


3. **Access the application:**
- Visit `http://localhost:5000/hello` to increment the user visit count.
- Access `http://localhost:5000/` to see a simple greeting.

## Technologies Used
- **Flask:** A lightweight WSGI web application framework.
- **MongoDB:** A NoSQL database used for storing user visit counts.
- **Docker:** Containerization platform used to encapsulate the application environment.

## API Reference
### GET /hello
Returns a greeting and the current count of user visits.

### GET /
Returns a simple greeting message.

## How to Contribute
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/fooBar`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some fooBar'`).
5. Push to the branch (`git push origin feature/fooBar`).
6. Create a new Pull Request.
