# Blog API

This is a simple Blog API built with Django and Django REST Framework. The API allows users to perform CRUD operations (Create, Read, Update, Delete) on blog posts. Additionally, authentication is implemented so that only the author of a blog post can update or delete it.

## Features

- List all blogs.
- View details of a single blog.
- Create new blogs (only authenticated users).
- Update and delete blogs (only the author can update or delete their own posts).
- JWT Authentication.

## Tech Stack

- **Django**: Web framework used to build the API.
- **Django REST Framework**: Provides the tools for creating the API.
- **Simple JWT**: Used for JSON Web Token (JWT) authentication.

## Endpoints

### Public Endpoints

- `GET /api/blog-list/`: List all blogs.
- `GET /api/blog-details/<id>/`: Get details of a specific blog by `id`.

### Protected Endpoints (requires authentication)

- `POST /api/blog-create/`: Create a new blog.
- `PUT /api/blog-update/<id>/`: Update an existing blog (only the author can update).
- `DELETE /api/blog-delete/<id>/`: Delete a blog (only the author can delete).

### Authentication Endpoints

- `POST /api/token/`: Obtain a JWT access token.
- `POST /api/token/refresh/`: Refresh an expired JWT access token.

## Installation and Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2.Set up a virtual environment

```bash
py -m venv myenv
source myenv/bin/activate
```

### 3.Install the dependencies

```bash
pip install -r requirements.txt
```

### 4.Set up the Django project

```bash
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
```

### 5.Run the development server

```bash
py manage.py runserver
```
