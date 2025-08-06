# FastAPI REST API Assignment - Starter Code

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Task Management API",
    description="A simple REST API for managing tasks",
    version="1.0.0"
)

# Pydantic models for data validation
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    
    class Config:
        from_attributes = True

# In-memory storage (replace with database in production)
tasks_db = []
next_id = 1

# TODO: Implement your API endpoints here

@app.get("/")
async def root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Task Management API"}

# TODO: Add GET /tasks endpoint

# TODO: Add POST /tasks endpoint

# TODO: Add GET /tasks/{task_id} endpoint

# TODO: Add PUT /tasks/{task_id} endpoint

# TODO: Add DELETE /tasks/{task_id} endpoint

if __name__ == "__main__":
    # Run the server
    uvicorn.run(app, host="127.0.0.1", port=8000)
