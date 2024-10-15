# Document Summarization Web Application

# Overview
This web application allows users to upload documents in various formats (PDF, DOCX, TXT) and receive summarized versions of those documents. The backend is powered by Flask/FastAPI, with a pre-trained language model (e.g., GPT-2) deployed locally to handle the summarization. The frontend is built with React, providing an intuitive interface for document uploads and displaying summaries.

# Features
- **File Upload:** Supports PDF, DOCX, and TXT formats.
- **Document Summarization:** Summarizes uploaded documents using a locally deployed Language Model (LLM).
- **Real-time Feedback:** The frontend provides real-time feedback on the status of the uploaded file and the generated summary.
- **Concurrency Handling:** The backend can handle multiple concurrent requests efficiently.
- **Docker Support:** The application can be deployed locally using Docker and Docker Compose.

## Tech Stack
# Backend
- **Framework:** Flask/FastAPI
- **Language Model:** GPT-2 or similar (deployed locally)
- **Deployment:** Docker, Docker Compose
- **Concurrency:** FastAPI async capabilities (if using FastAPI)

### Frontend
- **Framework:** React
- **File Upload:** Axios for API calls
- **UI:** Simple, responsive design with real-time feedback

## Getting Started

### Prerequisites
- **Docker** and **Docker Compose** installed on your machine..
- **Git** installed.

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/mradulpaliwal/Lepide_Project.git
   cd document-summarization-app

