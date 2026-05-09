# Agents Mission Charter

## Core Principles
- **DDD (Domain-Driven Design)**: Focus on the domain model, bounded contexts, and ubiquitous language.
- **Clean Architecture**: Strict separation of concerns (Domain, Application, Infrastructure, Presentation).
- **Clean Code**: Readable, maintainable, and efficient code following SOLID, DRY, KISS, and YAGNI.
- **TDD (Test-Driven Development)**: Follow the Red-Green-Refactor cycle. Write tests before implementation.
- **Baby-steps**: Incremental, verifiable progress.
- **Software Craftsmanship**: Commitment to high-quality, professional-grade engineering.

## Architecture Specifications

### Backend (Python/FastAPI)
- **Pattern**: Clean Architecture.
- **Database**: PostgreSQL using SQLModel.
- **Storage**: MinIO for blob storage.
- **Tree Structure**: Adjacency List pattern for folders and documents.
- **Type Safety**: Strict typing with Mypy.
- **Validation**: Pydantic for DTOs and request validation.

### Frontend (Next.js)
- **Pattern**: Atomic Design (Atoms, Molecules, Organisms, Templates, Pages).
- **State Management**: TanStack Query (React Query) for server state.
- **Styling**: Tailwind CSS.
- **Type Safety**: TypeScript (Strict mode).
- **Validation**: Zod for schema validation.

### Infrastructure
- **Deployment**: Docker Compose (local development & target deployment).
- **Services**: PostgreSQL, MinIO.
- **Monorepo Structure**:
  - `server/`: FastAPI application.
  scale: 1
  - `client/`: Next.js application.

## Engineering Standards

### Git & Workflow
- **Branching Strategy**: Clear feature branching.
- **Commits**: Conventional Commits (feat:, fix:, docs:, style:, refactor:, test:, chore:).
- **Commits Policy**: Never commit secrets, credentials, or large binaries.

### Quality Control
- **Python**: Ruff (linting/formatting), Mypy (type checking).
- **TypeScript**: ESLint, Prettier.
- **Testing**: 
  - Backend: Pytest.
  - Frontend: Vitest/Playwright.
  - End-to-End: Playwright.

## Task Management
- Use `AGENTS.md` as the single source of truth.
- Update `AGENTS.md` whenever a new architectural decision or constraint is introduced.
