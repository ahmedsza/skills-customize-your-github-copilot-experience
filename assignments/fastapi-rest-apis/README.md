# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a complete REST API using the FastAPI framework to practice web development concepts, HTTP methods, data validation, and API documentation.

## 📝 Tasks

### 🛠️	Create Basic FastAPI Application

#### Description
Develop a FastAPI application that serves as a task management system with endpoints for creating, reading, updating, and deleting tasks. The API should handle JSON data and provide automatic documentation.

#### Requirements
Completed program should:

- Install and import FastAPI and uvicorn dependencies
- Create a FastAPI application instance
- Implement GET endpoint to retrieve all tasks
- Implement POST endpoint to create new tasks
- Include basic task model with id, title, description, and completed status
- Run the server locally and display automatic API documentation
- Handle basic error responses for invalid requests

### 🛠️	Add Advanced API Features

#### Description
Enhance your basic API with data validation, path parameters, query parameters, and proper HTTP status codes to create a production-ready REST API.

#### Requirements
Completed program should:

- Use Pydantic models for request/response data validation
- Implement PUT endpoint to update existing tasks
- Implement DELETE endpoint to remove tasks
- Add path parameters for task ID operations
- Include query parameters for filtering tasks (completed/pending)
- Return appropriate HTTP status codes (200, 201, 404, 422)
- Add error handling with descriptive error messages
- Include response models for consistent API responses
