# WebAppWithMicroservices

## Overview

WebAppWithMicroservices is a robust web application designed to demonstrate the principles of microservices architecture, leveraging Docker for containerization and Flask for rapid web development. This project integrates several modern development practices and technologies to provide a scalable, maintainable, and efficient web application.

## Purpose

The primary purpose of this project is to illustrate how a web application can be built using microservices architecture. This approach breaks down the application into smaller, independent services that communicate with each other, making the system more modular and easier to manage. Each microservice can be developed, deployed, and scaled independently, providing significant flexibility and resilience.

## Functionality

### User Authentication

The main application provides a user authentication system where users can register, log in, and manage their sessions. This involves securely storing user credentials, handling user sessions, and ensuring secure communication between the client and server.

### Microservices Integration

One of the microservices included in this project is a joke service, which generates and returns a joke to the main application. This service showcases how to integrate external APIs and demonstrates the power of microservices by offloading specific tasks to dedicated services.

### Containerization with Docker

Docker is used to containerize the entire application, including the main web application, the joke service, and the database. Docker Compose is employed to manage these containers, providing a seamless setup and deployment process.

## Project Structure

The project is organized into several key directories and files, each serving a specific purpose:

### Main Application (`app` Directory)

- **`__init__.py`**: This script initializes the Flask application, sets up the necessary configurations, and initializes extensions like SQLAlchemy for database interactions, Bcrypt for password hashing, and Flask-Login for managing user sessions. It also imports the routes to ensure they are registered with the application.

- **`routes.py`**: This script defines the routes for the web application. It includes routes for user registration (`/create_account`), login (`/login`), logout (`/logout`), and a welcome page (`/welcome`). The welcome page also fetches a joke from the joke microservice, showcasing inter-service communication.

- **`models.py`**: This script defines the database models using SQLAlchemy. The primary model is `User`, which includes fields for username, email, and password. The `User` model also integrates with Flask-Login to manage user authentication and session management.

- **`forms.py`**: This script contains form definitions for user registration and login using Flask-WTF. It defines the form fields, validators, and custom validation logic to ensure data integrity and security during user interactions.

- **`templates/`**: This directory contains the HTML templates for the web application. The `base.html` template serves as the base template for other pages, providing a consistent layout and styling. `login.html` is the template for the login page, while `welcome.html` is the template for the welcome page displayed after login.

- **`static/`**: This directory contains static files like CSS and images. `styles.css` includes styles for the web application, enhancing the user interface. `paint_background_image.webp` is a background image used to improve the visual appeal of the application.

### Joke Microservice (`joke_service` Directory)

- **`Dockerfile`**: This script defines the Docker image for the joke microservice. It sets up a Python environment, installs dependencies from `requirements.txt`, and specifies the command to run the Flask application.

- **`requirements.txt`**: This file lists the Python dependencies for the joke microservice, including Flask for web development and OpenAI for joke generation.

- **`app.py`**: This script is the main Flask application for the joke microservice. It defines a single route (`/joke`) that uses the OpenAI API to generate a joke and returns it as a JSON response. This microservice illustrates how to integrate third-party APIs and provides a scalable way to handle specific tasks.

### Configuration and Deployment

- **`Dockerfile`**: This script defines the Docker image for the main web application. It sets up the Python environment, installs dependencies from `requirements.txt`, and specifies the command to run the Flask application.

- **`docker-compose.yml`**: This configuration file manages the multi-container Docker application. It defines three services: `web` for the main application, `db` for the MySQL database, and `joke_service` for the joke microservice. It also sets up environment variables for database connectivity and API keys.

- **`requirements.txt`**: This file lists the Python dependencies for the main web application, including Flask, SQLAlchemy, Flask-Bcrypt, Flask-Login, and requests.

- **`config.py`**: This script contains configuration settings for the Flask application, such as secret keys and database URIs. It loads these settings from environment variables to ensure flexibility and security.

- **`run.py`**: This script is the entry point for running the Flask application. It imports the app from the `app` package and runs it if the script is executed directly, allowing the application to start.

## Setup Instructions

### Prerequisites

- Docker installed on your machine.
- Docker Compose installed on your machine.


