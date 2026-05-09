.PHONY: setup dev-server dev-client test-server test-client docker-up docker-down migrate clean help

# Directories
SERVER_DIR := server
CLIENT_DIR := client
DOCKER_COMPOSE := docker-compose

# Commands
PIP := pip
NPM := npm

help:
	@echo "Available commands:"
	@echo "  setup           - Install dependencies for both server and client"
	@echo "  dev-server      - Run FastAPI server with hot-reload"
	@echo "  dev-client      - Run Next.js development server"
	@echo "  test-server     - Run backend tests with pytest"
	@echo "  test-client     - Run frontend tests with vitest"
	@echo "  migrate         - Placeholder for database migrations (Alembic)"
	@echo "  docker-up       - Start Docker containers (DB, MinIO)"
	@echo "  docker-down     - Stop Docker containers"
	@echo "  clean           - Clean up caches and build artifacts"

setup:
	@echo "🚀 Setting up the workspace..."
	@echo "--- Backend Setup ---"
	cd $(SERVER_DIR) && $(PIP) install -e .
	@echo "--- Frontend Setup ---"
	cd $(CLIENT_DIR) && $(NPM) install
	@echo "✅ Setup complete."

dev-server:
	@echo "🚀 Starting FastAPI Server..."
	cd $(SERVER_FRDIR) && uvicorn src.main:app --reload || cd $(SERVER_DIR) && uvicorn src.main:app --reload

dev-client:
	@echo "🚀 Starting Next.js Client..."
	cd $(CLIENT_DIR) && $(NPM) run dev

test-server:
	@echo "🧪 Running Backend Tests..."
	cd $(SERVER_DIR) && pytest

test-client:
	@echo "🧪 Running Frontend Tests..."
	cd $(CLIENT_DIR) && $(NPM) run test

migrate:
	@echo "🔄 Running database migrations..."
	@# Placeholder for: cd $(SERVER_DIR) && alembic upgrade head
	@echo "Note: Alembic is not yet configured. This will be implemented in Phase 2."

docker-up:
	@echo "🐳 Starting Docker infrastructure..."
	$(DOCKER_COMPOSE) up -d

docker-down:
	@echo "🛑 Stopping Docker infrastructure..."
	$(DOCKER_COMPOSE) down

clean:
	@echo "🧹 Cleaning up..."
	cd $(SERVER_DIR) && find . -type d -name "__pycache__" -exec rm -rf {} +
	cd $(CLIENT_DIR) && rm -rf .next node_modules
	@echo "✅ Cleanup complete."
