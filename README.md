# HNG12 Stage 0 - Public API

## Description

This is a public API developed as part of the HNG12 internship Stage 0 task. It provides basic personal details, including:
- A registered email address  
- The current datetime in ISO 8601 format (with milliseconds precision)  
- A link to the GitHub repository containing the project  

## Technologies Used

- Python  
- FastAPI  
- Uvicorn  
- CORS Middleware  

## API Documentation

### Base URL  
http://127.0.0.1:8000

### Endpoint  
#### **GET /**  
**Description:** Retrieves basic information to check if the API is running.  

**Request Example:**  
GET http://127.0.0.1:8000/

**Response Format:**  
```json
{
  "email": "your email",
  "current_datetime": "2025-01-30T04:14:03.056Z",
  "github_url": "https://github.com/username/repo"
}
```

---


### Response Codes  
- `200 OK` – Request successful  
- `500 Internal Server Error` – Server issue  

## Local Development Setup  

### Prerequisites  
Ensure you have the following installed:  
- Python 3.x  
- pip  

### Steps to Set Up Locally  
1. **Clone the repository:**  
   ```sh
   git clone https://github.com/BlessOnyi/hng12-stage0-api.git
   cd hng12-stage0-api


2. **Create and Activate a Virtual Environment:**  
  python -m venv venv

  **Activate Environment**
- source venv/bin/activate  # On macOS/Linux
- venv\Scripts\activate  # On Windows


3. **Install dependencies:**
- pip install -r requirements.txt

4. **Run the development server:**
- uvicorn main:app --reload
- The API will be available at http://127.0.0.1:8000


## Deployment  

### To deploy this API using Render:  
1. **Create a new Web Service** on Render.  
2. **Connect your GitHub repository.**  


## Installation

1. **Install dependencies**  
   Run the following command to install all required dependencies:

   ```bash
   pip install -r requirements.txt


2. **Set the start command**
  uvicorn main:app --host 0.0.0.0 --port $PORT

3. **Environment Variables.**
  PORT: Server port (default: 8000)

## Live Demo

### The API is deployed at: https://hng12-stage0-ln1chyoy1-blessings-projects-b5288423.vercel.app/

### https://hng.tech/hire/python-developers




