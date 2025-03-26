# Masterblog-API

### Blog Post Management System

## Description
This project is a full-stack web application for managing blog posts. 
It features a Flask backend API and a JavaScript frontend, allowing users to create, read, delete, and search blog posts.

## Features
- Create new blog posts with title, content, author, and date
- View all blog posts
- Delete existing blog posts
- Search posts by content
- Responsive design for various screen sizes

## Technologies Used
- Backend:
  - Python 3.x
  - Flask
  - SQLite
- Frontend:
  - HTML5
  - CSS3
  - JavaScript (ES6+)

## Setup and Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/EcoG-One/Masterblog-API.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ``` 
3. Run the backend app:
   ```bash
   python backend/backend_app.py
   ```
The backend server will start running on `http://localhost:5002`.

### Frontend Setup
Run the frontend application:
```bash
    python frontend/frontend_app.py
```
The frontend server will start running on `http://localhost:5001`.

## Usage
1. Open a web browser and go to `http://localhost:5001`.
2. If not there, enter the backend API URL (`http://localhost:5002`) in the provided input field and click "Load Posts".
3. Use the interface to add new posts, view existing posts, delete posts, and search for posts.

## API Endpoints

- `GET /posts`: Retrieve all posts
- `POST /posts`: Create a new post
- `DELETE /posts/<post_id>`: Delete a specific post
- `GET /posts/search/<query>`: Search for posts containing the query string