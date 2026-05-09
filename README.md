# DocManager 📄

A robust, enterprise-grade document management system built with a commitment to Software Craftsmanship. This project implements advanced architectural patterns to ensure scalability, maintainability, and testability.

## 🚀 Tech Stack

### Backend
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Python 3.11+)
- **Architecture**: Clean Architecture & Domain-Driven Design (DDD)
- **Database**: [PostgreSQL](https://www.postgresql.org/) with [SQLModel](https://sqlmodel.tiangolo.com/) (SQLAlchemy + Pydantic)
- **Object Storage**: [MinIO](https://min.io/) (S3-compatible)
- **Testing**: [Pytest](https://docs.pytest.org/) (TDD approach)
- **Linting/Typing**: Ruff, Mypy

### Frontend
- **Framework**: [Next.js](https://nextjs.org/) (React)
- **Architecture**: [Atomic Design](https://bradfrost.com/blog/post/atomic-web-design/) (Atoms, Molecules, Organisms, Templates, Pages)
- **State Management**: [TanStack Query](https://tanstack.com/query/latest) (React Query)
- **Stylest**: [Tailwind CSS](https://tailwindcss.com/)
- **Validation**: [Zod](https://zod.dev/)
- **Testing**: [Vitest](https://vitest.dev/), [Playwright](httpsertest.dev/)

### Infrastructure
- **Orchestration**: [Docker Compose](https://docs.docker.com/compose/)
- **Monorepo Structure**: `server/` (Backend) and `client/` (Frontend)

## 🛠 Engineering Principles

This project is built strictly following:
- **DDD (Domain-Driven Design)**: Focusing on the domain model and ubiquitous language.
- **Clean Architecture**: Strict separation between Domain, Application, Infrastructure, and Presentation layers.

- **TDD (Test-Driven Development)**: We follow the Red-Green-Refactor cycle. No logic is implemented without a failing test first.
- **Software Craftsmanship**: Adherence to SOLID, DRY, KISS, and YAGNI principles.
- **Code Quality**: High emphasis on type safety, comprehensive testing (Unit, Integration, E2E), and clean, readable code.

## 🏁 Getting Started

### Prerequisites
- [Docker & Docker Compose](https://docs.docker.com/get-docker/)
- [Python 3.11+](https://www.python.org/)
- [Node.js & npm/yarn](https://nodejs.org/)
- [Make](https://www.gnu.org/software/make/)

### Installation & Setup
The project uses a `Makefile` to orchestrate the workspace.

1. **Clone the repository**
   ```bash
   git clone <repo_url>
   cd doc-manager
   ```

2. **Spin up the infrastructure (PostgreSQL & MinIO)**
   ```bash
   make docker-up
   ```

3. **Setup the workspace** (installs dependencies for both client and server)
   ```bash
   make setup
   ```

### Development Workflow

#### Running the Servers
- **Backend**: `make dev-server`
- **Frontend**: `make dev-client`

#### Running Tests
- **Backend Tests**: `make test-server`
- **Frontend Tests**: `make test-client`

#### Database Migrations
*(Note: Migrations implemented via Alembic in Phase 2)*
```bash
make migrate
```

## 📂 Project Structure

```text
.
├── client/             # Next.js Application (Atomic Design)
├── server/             # FastAPI Application (Clean Architecture)
│   ├── src/
│   │   ├── domain/      # Core business logic & Entities
│   │   ├── application/ # Use Cases & Service interfaces
│   │   ├── infrastructure/ # Persistence (SQLModel) & Storage (MinIO)
│   │   └── presentation/ # API Routes & Controllers
│   └── tests/          # Backend Test Suite
├── docker-compose.yml  # Infrastructure setup
├── Makefile            # Workspace orchestrator
├── AGENTS.md           # Project guidelines & constraints
└── README.md           # Project documentation
```

## 📜 Git Contribution Policy

We follow **Conventional Commits**.
- `feat:` A new feature.
- `fix:` A bug fix.
- `docs:` Documentation only changes.
- `style:` Changes that do not affect the meaning of the code (white-space, formatting, etc).
- `refactor:` A code change that neither fixes a bug nor adds a feature.
- `test:` Adding missing tests or correcting existing tests.
- `chore:` Changes to the build process or auxiliary tools and libraries.

Please use feature branches (e.g., `feature/auth-module`) and submit Pull Requests for review.
