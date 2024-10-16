# Full Stack React Application

This project consists of a React frontend and a Python-based backend.

## Frontend

The frontend is a React application created with Create React App.

### Frontend Setup

1. Navigate to the frontend directory:
cd frontend


2. Install dependencies:
npm install


### Frontend Scripts

- Start the development server:
npm start


- Run tests:
npm test



- Build for production:
npm run build


## Backend

The backend is a Python-based application.

### Backend Setup

1. Create a virtual environment:
python -m venv venv


2. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

3. Install required dependencies (add dependencies in `requirements.txt` as necessary):
pip install -r requirements.txt


### Backend Scripts

- Start the backend server:
python manage.py runserver

- Run backend tests:
python manage.py test



### GROQ API Setup

This project integrates with the Groq API. To use the API, you'll need to set up your own `GROQ_API_KEY`.

1. Obtain your `GROQ_API_KEY` by signing up for the Groq API at their official website.

2. Once you have the key, add it to your environment variables or include it in your application’s configuration. For local development, you can set it by creating a `.env` file in the root of your backend directory with the following contents:
GROQ_API_KEY=your_key_here


3. Ensure that your application reads the key from the environment:
```python
import os

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
'''
