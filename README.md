# FastAPI Template

> **Note:** This project is primarily a personal template created for my own learning and to speed up the bootstrap process for my future ideas. While it is tailored to my workflow, if you stumble upon this repository, feel free to explore it! Constructive feedback and suggestions are always welcome.

## Overview

This is a modular project template designed for building scalable applications that require a REST API, a Telegram Bot, and a robust event-driven architecture. It comes pre-configured with a modern tech stack and containerized infrastructure.

## 🛠 Tech Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python 3.13+)
- **Bot:** Python (ready for [aiogram](https://docs.aiogram.dev/))
- **Database:** PostgreSQL (with `asyncpg`)
- **Caching & Broker:** Redis
- **Event Streaming:** Kafka & Zookeeper
- **Package Management:** [uv](https://github.com/astral-sh/uv)
- **Infrastructure:** Docker & Docker Compose

## 📂 Project Structure

```plaintext
.
├── backend/            # FastAPI application
│   ├── src/            # Application source code (api, models, schemas)
│   └── main.py         # Entry point
├── bot/                # Telegram Bot application
│   ├── components/     # Bot components
│   └── main.py         # Entry point
├── frontend/           # Frontend application (placeholder)
├── docker-compose.yml  # Local infrastructure orchestration
├── pyproject.toml      # Project dependencies
└── uv.lock             # Lock file
```

## 🚀 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) and Docker Compose
- [uv](https://github.com/astral-sh/uv) (optional, for local development without Docker)

### Running with Docker (Recommended)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/fastapi-template.git
    cd fastapi-template
    ```

2.  **Configure Environment:**
    Copy the example environment file and adjust the values if necessary.
    ```bash
    cp .env.example .env
    ```

3.  **Start the services:**
    Build and run the containers.
    ```bash
    docker-compose up --build
    ```

    This will start:
    - **Backend** at `http://localhost:8000`
    - **PostgreSQL** at `localhost:5432`
    - **Redis** at `localhost:6379`
    - **Kafka** at `localhost:9092`
    - **Bot** service

### Local Development

If you want to run the services locally without Docker containers for the code:

1.  **Install dependencies:**
    ```bash
    uv sync
    ```

2.  **Activate virtual environment:**
    ```bash
    source .venv/bin/activate
    ```

3.  **Run Backend:**
    ```bash
    uvicorn backend.main:app --reload
    ```

4.  **Run Bot:**
    ```bash
    python -m bot.main
    ```

## 📝 Todo / Roadmap

- [ ] Set up Alembic migrations
- [ ] Implement basic API endpoints
- [ ] Add Pydantic schemas
- [ ] Configure CI/CD pipelines
- [ ] Add frontend implementation

## 🤝 Feedback

If you have any suggestions on how to improve the architecture or code quality, please feel free to open an issue or submit a pull request.
