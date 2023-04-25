 
import os

# Define the directory and subdirectory names
dashboard_directory = 'chatbot_analytics_dashboard'
backend_directory = 'backend'
frontend_directory = 'frontend'
data_directory = 'data'

# Create the main directory for the project
if not os.path.exists(dashboard_directory):
    os.mkdir(dashboard_directory)

# Create the backend directory and files
backend_directory_path = os.path.join(dashboard_directory, backend_directory)
if not os.path.exists(backend_directory_path):
    os.mkdir(backend_directory_path)
open(os.path.join(backend_directory_path, '__init__.py'), 'w').close()
open(os.path.join(backend_directory_path, 'main.py'), 'w').close()

# Create the frontend directory and files
frontend_directory_path = os.path.join(dashboard_directory, frontend_directory)
if not os.path.exists(frontend_directory_path):
    os.mkdir(frontend_directory_path)
open(os.path.join(frontend_directory_path, '__init__.py'), 'w').close()
open(os.path.join(frontend_directory_path, 'main.py'), 'w').close()

# Create the data directory
data_directory_path = os.path.join(dashboard_directory, data_directory)
if not os.path.exists(data_directory_path):
    os.mkdir(data_directory_path)
