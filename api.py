"""
FastAPI backend for Task Management System
This module provides API endpoints for managing tasks in a simple task management system.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uvicorn

app = FastAPI(title="Task Management API")

# Pydantic model for Task
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    status: str
    due_date: str
    priority: str

# In-memory storage for tasks
tasks_db = []
task_counter = 1

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    """
    Retrieve all tasks from the database
    Returns:
        List[Task]: List of all tasks
    """
    return tasks_db

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    """
    Create a new task
    Args:
        task (Task): Task object containing task details
    Returns:
        Task: Created task with assigned ID
    """
    global task_counter
    task.id = task_counter
    task_counter += 1
    tasks_db.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    """
    Update an existing task
    Args:
        task_id (int): ID of the task to update
        updated_task (Task): Updated task details
    Returns:
        Task: Updated task
    """
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            updated_task.id = task_id
            tasks_db[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """
    Delete a task
    Args:
        task_id (int): ID of the task to delete
    Returns:
        dict: Success message
    """
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(i)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
