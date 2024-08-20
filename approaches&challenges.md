# Approach and Challenges

## Approach

### 1. Backend (Flask/FastAPI)
- **Framework Selection:** We chose Flask/FastAPI for its lightweight nature and ease of setting up RESTful endpoints.
- **File Handling:** The `/upload` endpoint handles PDF, DOCX, and TXT files. We ensured proper validation and storage mechanisms.
- **LLM Integration:** We integrated a pre-trained model (e.g., GPT-2) using Hugging Face's `transformers` library to generate text summaries.
- **Concurrency Handling:** We leveraged async functionality in FastAPI to handle multiple concurrent requests efficiently.

### 2. Frontend (React)
- **UI Design:** We created a simple file upload form with intuitive user feedback for success or errors. The summarized text is displayed in a clean and readable format.
- **API Interaction:** The frontend communicates with the backend via RESTful API calls using `axios`.

### 3. Docker Deployment
- **Dockerization:** We containerized both backend and frontend using Docker. The Docker Compose file orchestrates both services for easy local deployment.

## Challenges Faced

### 1. Model Deployment
- **Challenge:** Deploying a pre-trained LLM locally was resource-intensive and required optimization to handle large text inputs.
- **Solution:** We optimized the model using techniques like reducing token length and utilizing batch processing to improve performance.

### 2. Concurrency Management
- **Challenge:** Ensuring the backend could handle multiple requests simultaneously, especially when processing large documents.
- **Solution:** FastAPI’s async capabilities allowed us to manage concurrency efficiently.

### 3. File Upload Validation
- **Challenge:** Handling different file formats (PDF, DOCX, TXT) and ensuring smooth file parsing and error handling.
- **Solution:** We implemented a robust validation system to check file types and handle parsing errors gracefully.