# Setup Instructions

## Prerequisites
1. Install **Docker** and **Docker Compose**.
2. Ensure you have **Git** installed.

## Clone the Repository
```bash
git clone https://github.com/mradulpaliwal/Lepide_Project.git
cd document-summarization-app
##  Running the Application Locally
# 1. Using Docker Compose (Recommended)
#To build and start both the backend and frontend services, use Docker Compose:
docker-compose up --build
## 2. Running Backend Locally (Without Docker)
# 1.Navigate to the backend/ directory:
cd backend
# 2.Install the dependenciees
pip install -r requirements.txt
## 3.pip install -r requirements.txt
python app.py
## 3. Running Frontend Locally (Without Docker)
# 1.Navigate to the frontend/ directory:
cd frontend
# 2.Install the dependencies:
npm install
# 3.Start the React application:
npm start

