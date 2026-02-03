# Microservices Task Manager

A simple task management application with Python Flask microservices and multistage Docker builds.

## Architecture

- **Backend Service**: Flask REST API (Port 5001)
- **Frontend Service**: Flask web app with nice UI (Port 3000)
- **Multistage Docker**: Optimized builds with separate build and production stages

## Quick Start

```bash
# Start both services
docker-compose up --build

# Access the app
# Frontend: http://localhost:3000
# Backend API: http://localhost:5001
```

## Features

- Create, update, delete tasks
- Modern UI with Tailwind CSS
- REST API backend
- Multistage Docker builds for smaller images

## Project Structure

```
├── backend/
│   ├── app.py           # Flask API
│   ├── requirements.txt # Dependencies
│   └── Dockerfile      # Multistage Docker build
├── frontend/
│   ├── app.py          # Flask web server
│   ├── templates/      # HTML templates
│   └── Dockerfile     # Multistage Docker build
└── docker-compose.yml  # Run both services
```

## Multistage Docker Benefits

- **Build stage**: Installs dependencies with pip
- **Production stage**: Only copies installed packages and code
- **Smaller images**: No build tools in final image
- **Faster deployments**: Cleaner production containers

## API Endpoints

- `GET /api/tasks` - Get all tasks
- `POST /api/tasks` - Create task
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task