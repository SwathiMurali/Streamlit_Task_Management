# Streamlit Task Management Demo

This project demonstrates various features of Streamlit integrated with FastAPI backend. It's a simple task management system that showcases different Streamlit widgets, layouts, and API integration.

## Features Demonstrated

1. **Streamlit Features**
   - Page configuration and layout
   - Forms and input widgets
   - Data display with pandas DataFrames
   - Interactive components
   - Sidebar navigation
   - Custom styling
   - API integration

2. **FastAPI Features**
   - RESTful API endpoints
   - Pydantic models for data validation
   - CRUD operations
   - Async request handling

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install dependencies:
   ```powershell
   pip install streamlit fastapi uvicorn pandas requests
   ```

## Running the Application

1. Start the FastAPI backend:
   ```powershell
   uvicorn api:app --reload
   ```

2. In a new terminal, start the Streamlit frontend:
   ```powershell
   streamlit run app.py
   ```

3. Open your browser and navigate to:
   - Streamlit UI: http://localhost:8501
   - FastAPI docs: http://localhost:8000/docs

## Project Structure

- `api.py`: FastAPI backend with task management endpoints
- `app.py`: Streamlit frontend application
- `README.md`: Project documentation
