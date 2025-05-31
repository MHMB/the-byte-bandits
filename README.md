# The Byte Bandits: AI Investment Advisor Chatbot

## Project Overview

**The Byte Bandits** is an AI-powered investment advisor platform featuring a modern chatbot interface. The system consists of a FastAPI backend serving as a robo-advisor and a Streamlit frontend for real-time, user-friendly chat interactions. The backend leverages MongoDB and Redis for data storage and caching, and the entire stack can be run locally or via Docker Compose.

## Features
- **Conversational AI**: Chatbot interface for investment advice and portfolio management.
- **FastAPI Backend**: Robust REST API for chat, user, and portfolio management.
- **Streamlit Frontend**: Elegant, real-time chat UI with RTL (right-to-left) support.
- **Persistence**: MongoDB for data storage, Redis for caching.
- **Dockerized**: Easy deployment with Docker Compose, including Traefik for routing.

## Project Structure
```
├── backend
│   ├── main.py           # FastAPI entry point
│   ├── api/              # API routers (chat, user, portfolio)
│   ├── db/               # Database connectors (MongoDB)
│   └── ...
├── frontend
│   └── src/
│       ├── app.py        # Streamlit app entry point
│       └── utils/        # Frontend utilities
├── docker/
│   ├── Dockerfile        # Backend Dockerfile
│   └── Dockerfile.frontend # Frontend Dockerfile
├── docker-compose.yml    # Multi-service orchestration
├── pyproject.toml        # Backend dependencies (Poetry)
├── frontend/requirements.txt # Frontend dependencies
└── README.md
```

## Local Development Setup

### Prerequisites
- Python 3.12 (backend) and Python 3.10+ (frontend)
- [Poetry](https://python-poetry.org/) for backend dependency management
- [Node.js](https://nodejs.org/) (optional, for advanced frontend dev)
- MongoDB and Redis running locally (or use Docker Compose)

### 1. Backend Setup
```bash
# Install Python 3.12 and Poetry
# (see https://github.com/pyenv/pyenv and https://python-poetry.org/docs/)

# Clone the repo and enter the directory
$ git clone <repository-url>
$ cd test-byte-bandits

# Set up Python environment (using pyenv/poetry)
$ pyenv install 3.12.2
$ pyenv virtualenv 3.12.2 the-byte-bandits_env_3.12.2
$ pyenv activate the-byte-bandits_env_3.12.2
$ pyenv local the-byte-bandits_env_3.12.2

# Install backend dependencies
$ poetry install --no-dev

# Set up environment variables (see .env.example or .env)

# Run the backend API
$ cd backend
$ poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Frontend Setup
```bash
# In a new terminal, from the project root
$ cd frontend
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

# Run the Streamlit app
$ streamlit run src/app.py
```

The frontend will be available at [http://localhost:8501](http://localhost:8501).

---

## Docker Setup (Recommended)

### 1. Prerequisites
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)

### 2. Environment Variables
Copy `.env.example` to `.env` and adjust ports and secrets as needed.

### 3. Start All Services
```bash
$ docker-compose up --build
```
- Backend: [http://localhost:8000](http://localhost:8000)
- Frontend: [http://localhost:8501](http://localhost:8501)
- Traefik Dashboard: [http://localhost:8080](http://localhost:8080) (if enabled)

This will launch:
- FastAPI backend (with MongoDB and Redis)
- Streamlit frontend
- Traefik reverse proxy

---

## Usage
- Open your browser to [http://localhost:8501](http://localhost:8501) to interact with the chatbot.
- The backend API is accessible at [http://localhost:8000/docs](http://localhost:8000/docs) for OpenAPI documentation.

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
