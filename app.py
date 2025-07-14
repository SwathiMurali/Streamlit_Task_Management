"""
Streamlit Task Management Application
This module demonstrates various Streamlit features through a task management interface.
"""
import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import json

# Configure page settings
st.set_page_config(
    page_title="Task Management Demo",
    page_icon="✅",
    layout="wide"
)

# Custom CSS to enhance the UI
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton button {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar with app information
with st.sidebar:
    st.title("🎯 Task Manager")
    st.markdown("### Features Demo")
    st.markdown("""
    This application demonstrates various Streamlit features:
    - 📊 Data display
    - 🎨 Layouts and containers
    - 🔄 API integration
    - 📝 Forms and inputs
    - 🎯 Interactive widgets
    """)

# API endpoint
API_URL = "http://127.0.0.1:8000"

def fetch_tasks():
    """Fetch all tasks from the API"""
    try:
        response = requests.get(f"{API_URL}/tasks")
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error fetching tasks: {str(e)}")
        return []

def create_task(task_data):
    """Create a new task via API"""
    try:
        response = requests.post(f"{API_URL}/tasks", json=task_data)
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error creating task: {str(e)}")
        return None

def delete_task(task_id):
    """Delete a task via API"""
    try:
        response = requests.delete(f"{API_URL}/tasks/{task_id}")
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error deleting task: {str(e)}")
        return None

# Main content
st.title("📋 Task Management System")

# Create two columns for layout
col1, col2 = st.columns([2, 1])

with col2:
    # Task creation form using st.form
    with st.form("task_form", clear_on_submit=True):
        st.subheader("Create New Task")
        
        title = st.text_input("Task Title")
        description = st.text_area("Description")
        
        # Date input with default value
        due_date = st.date_input("Due Date")
        
        # Select boxes for status and priority
        status = st.selectbox(
            "Status",
            ["Not Started", "In Progress", "Completed"]
        )
        
        priority = st.selectbox(
            "Priority",
            ["Low", "Medium", "High"]
        )
        
        submitted = st.form_submit_button("Create Task")
        
        if submitted:
            if title and description:
                task_data = {
                    "title": title,
                    "description": description,
                    "due_date": due_date.strftime("%Y-%m-%d"),
                    "status": status,
                    "priority": priority
                }
                
                if create_task(task_data):
                    st.success("Task created successfully!")
            else:
                st.warning("Please fill in all required fields.")

with col1:
    st.subheader("Task List")
    
    # Add refresh button
    if st.button("🔄 Refresh Tasks"):
        st.experimental_rerun()
    
    # Fetch and display tasks
    tasks = fetch_tasks()
    
    if tasks:
        # Convert tasks to DataFrame for better display
        df = pd.DataFrame(tasks)
        
        # Add color coding based on priority
        def color_priority(val):
            colors = {
                "High": "red",
                "Medium": "orange",
                "Low": "green"
            }
            return f'color: {colors.get(val, "black")}'
        
        # Style the DataFrame
        styled_df = df.style.applymap(
            color_priority,
            subset=['priority']
        )
        
        # Display tasks in an interactive table
        st.dataframe(
            styled_df,
            column_config={
                "id": "ID",
                "title": "Title",
                "description": "Description",
                "status": "Status",
                "due_date": "Due Date",
                "priority": "Priority"
            },
            hide_index=True
        )
        
        # Task deletion
        st.subheader("Delete Task")
        task_to_delete = st.selectbox(
            "Select task to delete",
            options=df['id'].tolist(),
            format_func=lambda x: f"Task {x}: {df[df['id'] == x]['title'].iloc[0]}"
        )
        
        if st.button("Delete Selected Task"):
            if delete_task(task_to_delete):
                st.success("Task deleted successfully!")
                st.experimental_rerun()
    else:
        st.info("No tasks found. Create a new task to get started!")
